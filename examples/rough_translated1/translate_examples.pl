#!/bin/env perl

use strict;
use warnings;

my $examples_source_folder = 
    "F:/Users/cmbruns/build/OpenSceneGraph-3.2.1/OpenSceneGraph-3.2.1/examples";
    # "C:/Users/cmbruns/git/osg/examples";
translate_all_examples($examples_source_folder);

# Translates one C++ source file into python
sub translate_source_file {
    my $file = shift;
    die unless open( my $fh, $file );
    my $file_block = join("", <$fh>); # Read entire file at once

    # TODO - break these task blocks into separate subroutines

    # Parse osg modules used, from headers
    # #include <osg/ApplicationUsage>
    my %modules = ();
    while ( $file_block =~ m/^#include\s+[<"](\w+)\//mg ) {
        $modules{$1} += 1;
    }
    while (my ($mod, $count) = each %modules ) {
        # debugging loop
        # print $mod, ": ", $count, "\n";
    }

    # Strip away osg::ref_ptr<...> shell
    # osg::ref_ptr<whatever> is already secretly inside the python classes
    $file_block =~ s/osg::ref_ptr<([^>]+)>/$1/g;

    # Replace literal C characters with integers
    $file_block =~ s/'(.)'/ord("$1")/g;

    # Logical OR/AND/NOT
    $file_block =~ s/\|\|/ or /g;      
    $file_block =~ s/&&/ and /g;     
    $file_block =~ s/!/ not /g;

    # Regexes can only do finite nesting of parentheses
    my $paren_rx = "\\([^()]*\\)";
    my $paren2_rx = "\\((?:[^()]*${paren_rx})*[^()]*\\)";
    my $paren3_rx = "\\((?:[^()]*${paren2_rx})*[^()]*\\)";
    my $paren4_rx = "\\(((?:[^()]*${paren3_rx})*[^()]*)\\)"; # capture insides

    # Regular expressions to help (mostly) identify function declarations
    my $ident_rx = "[a-zA-Z_][a-zA-Z0-9_]*"; # identifiers
    my $type_rx = "(?:$ident_rx\\:\\:)*$ident_rx(?:<.*>)?"; # type names
    my $dec_type_rx = "(?:(?:virtual|const|unsigned)\\s+)*$type_rx(?:\\s*\\*+|&)?"; # type names
    my $arg_ident_rx = "(?:\\*+|&)?($ident_rx)"; # e.g. "**argv"
    my $funcarg_rx = "$dec_type_rx\\s+$arg_ident_rx(\\s*=\\s*\\S+)?"; # one argument to a function
    my $funcargs_rx = "\\(\\s*($funcarg_rx(?:\\s*,\\s*$funcarg_rx)*)?\\s*\\)"; # parentheses and arguments to a function
    my $func_rx = "^(\\s*)$dec_type_rx\\s+($ident_rx)\\s*$funcargs_rx\\s*(?:const\\s*)?{";

    # Translate class declarations, like
    # "class PlaneConstraint : public osgManipulator::Constraint {"
    my $class_rx = "^(\\s*)(?:class|struct)\\s+($ident_rx)\\s*(?:\:\\s*(?:public\\s*)?($type_rx)\\s*)?{\\s*";
    while ( $file_block =~ m/($class_rx)/mg ) {
        my $cpp_class = $1;
        my $indent = $2;
        my $cls_name = $3;
        my $py_class = "${indent}class $cls_name";
        if (defined $4) {
            $py_class .= " ($4)";
        }
        $py_class .= " :\n";
        # print "$cpp_class\n";
        # print "$py_class\n";
        $file_block =~ s/\Q${cpp_class}/${py_class}/;
    }
    $file_block =~ s/\n\s*(public|protected|private)://g;
    $file_block =~ s/(public|protected|private)://g;

    # Loop for debugging...
    while ( $file_block =~ m/($func_rx)/mg ) {
        # print "$1\n";
    }

    # Translate function declarations
    # Like "int main(int foo) {"
    while ( $file_block =~ m/($func_rx)/mg ) {
        my $cpp_func = $1;
        my $indent = $2;
        my $fn_name = $3;
        my @arg_names = ();
        my $all_args = $4;
        if (defined $all_args) {
            my @args = split ",", $all_args;
            foreach my $arg (split ",", $all_args) {
                $arg =~ m/^\s*$funcarg_rx\s*$/;
                my $arg_name = $1;
                # my $equals = $2;
                # print $1, "\n"
                push @arg_names, $1;
            }
        }
        my $py_func = "${indent}def $fn_name(";
        $py_func .= join ", ", @arg_names;
        $py_func .= "):\n$indent    ";

        # print $cpp_func, "\n";
        # print $py_func;
        $file_block =~ s/\Q${cpp_func}/${py_func}/;
    }

    my $dec_ass_rx = "(^([\\t\ ]*)$dec_type_rx\\s+$arg_ident_rx\\s*=\\s*([^;]*);)";

    # Translate declare-and-assign; "int foo = 3;"
    while ( $file_block =~ m/$dec_ass_rx/mg) {
        my $cpp_ass = $1;
        my $indent = $2;
        my $ident = $3;
        my $rhs = $4;
        # We will remove the semicolon later
        my $py_ass = "$indent$ident = $rhs;";
        # print $cpp_ass, "\n";
        # print $py_ass, "\n";
        $file_block =~ s/\Q${cpp_ass}/${py_ass}/;
    }

    # Declare and initialize implicitly "Bar foo;"
    my $dec_init_rx0 = "^([\\t\ ]*)($dec_type_rx)\\s+($arg_ident_rx)\\s*\\s*;";
    while ( $file_block =~ m/($dec_init_rx0)/mg) {
        my $cpp_dec = $1;
        my $indent = $2;
        my $type = $3;
        my $ident = $4;
        # No keywords
        next if $type =~ m/^return$/;
        # We will remove the semicolon later
        my $py_dec = "$indent$ident = $type();";
        # print $cpp_dec, "\n";
        # print $py_dec, "\n";
        $file_block =~ s/\Q${cpp_dec}/${py_dec}/;
    }

    # Declare and initialize "Bar foo(3);"
    my $dec_init_rx = "^([\\t\ ]*)($dec_type_rx)\\s+($arg_ident_rx)\\s*($paren4_rx)\\s*;";
    while ( $file_block =~ m/($dec_init_rx)/mg) {
        my $cpp_dec = $1;
        my $indent = $2;
        my $type = $3;
        my $ident = $4;
        my $init = $6;
        # We will remove the semicolon later
        my $py_dec = "$indent$ident = $type$init;";
        # print $cpp_dec, "\n";
        # print $py_dec, "\n";
        $file_block =~ s/\Q${cpp_dec}/${py_dec}/;
    }

    # "new" constructor
    $file_block =~ s/\bnew\b\s*([^;()]*\S)\s*;/$1();/g; # "new" no parentheses
    $file_block =~ s/\bnew\b\s*//g; # "new" already with parentheses

    # If/While statements
    my $ifwhile_rx = "(else\\s+if|if|while)\\s*$paren4_rx";
    while ( $file_block =~ m/($ifwhile_rx)/mg) {
        my $cpp_while = $1;
        # print "$1\n";
        # strip one set of parentheses
        my $kw = $2;
        my $contents = $3;
        if ($kw =~ /^else/) {$kw = "elif";}
        #
        my $py_while = "$kw $contents :";
        # print $cpp_while, "\n";
        # print $py_while, "\n";
        $file_block =~ s/\Q${cpp_while}/${py_while}/;
    }

    $file_block =~ s/\belse\b(?:[ {\t]*\n)/else:\n/g;

    # Ternary operator, after initial "if" pass
    $file_block =~ s/(${paren4_rx}|\S+)\s*\?\s*(.*\S)\s*:/ $3 if ($1) else /g;

    # Translate console output statements
    $file_block =~ s/(?:std::)?cout\s*<<\s*/print /g;
    $file_block =~ s/\s*<<\s*(?:std::)?endl//g;
    $file_block =~ s/\s*<<\s*/, /g;

    # Translate string classes
    $file_block =~ s/std::string/str/g;

    # Convert comments from "//" and "/* */" to "#"
    # http://blog.ostermiller.org/find-comment
    while ( $file_block =~ m!(/\*((?:.|[\r\n])*?)\*/)!mg ) {
        my $cpp_comment = $1;
        my $py_comment = "#$2";
        $py_comment =~ s/\n/\n#/g;
        # print $cpp_comment, "\n";
        # print $py_comment, "\n";
        $file_block =~ s/\Q${cpp_comment}/${py_comment}/;
    }
    $file_block =~ s!//!#!g;
    # $file_block =~ s!/\*!#!g;
    # $file_block =~ s!\*/!!g;

    # Convert membership operators
    $file_block =~ s/->/./g;
    $file_block =~ s/::/./g;

    # Remove semicolons, braces
    $file_block =~ s/(?<=\n)[\ \t]*{[\ \t]*\n//g; # brace on its own line
    $file_block =~ s/(?<=\n)[\ \t]*}[\ \t]*\n//g; # brace on its own line
    $file_block =~ s/[{};]//g; # other braces and semicolons

    # Remove const, references
    $file_block =~ s/\bconst\b//g;
    $file_block =~ s/&//g;

    # true/false
    $file_block =~ s/\btrue\b/True/g;
    $file_block =~ s/\bfalse\b/False/g;   

    # floating point numbers, like "1.0f"
    $file_block =~ s/\b([-+0-9\.]+)[f]\b/$1/g;

    # Smart pointer ".get()" methods are superfluous
    $file_block =~ s/\.get\(\)//g;

    # argv converions
    $file_block =~ s/\Qdef main(argc, argv):/def main(argv):/g;
    $file_block =~ s/ArgumentParser\(argc,\s*argv\)/ArgumentParser(argv)/g;

    return $file_block, \%modules;
}

# Translates one OpenSceneGraph example folder from C++ to python
sub translate_example {
    my $example = shift;
    my $folder = shift;
    die unless opendir( my $dh, $folder);
    my %osg_modules = ();
    my @file_blocks = ();
    while (readdir $dh) {
        my $file = "$folder/$_";
        next unless -f $file; # Files only, please
        next unless $_ =~ m/\.[ch]/; # C++ source files only, please
        print "  Translating source file: ", $_, "\n";
        my ($source_block, $modules) = translate_source_file($file);
        while (my ($mod, $count) = each %{$modules}) {
            # print "$mod: $count\n";
            $osg_modules{$mod} += $count;
        }
        $source_block = "\n# Translated from file '$_'\n\n" . $source_block;
        push @file_blocks, $source_block;
    }
    die unless open( my $pyfh, ">$example.py" );

    my $header = << "EOM";
#!/bin/env python

# Automatically translated python version of 
# OpenSceneGraph example program "$example"
# !!! This program will need manual tuning before it will work. !!!

import sys

EOM
    print $pyfh $header;

    foreach my $osgmodule (sort keys %osg_modules) {
        print $pyfh "from osgpypp import $osgmodule\n"
    }
    print $pyfh "\n";

    foreach my $block (@file_blocks) {
        print $pyfh $block;
    }
    my $footer = << 'EOM';


if __name__ == "__main__":
    main(sys.argv)
EOM
    print $pyfh $footer;
    close($pyfh);
    closedir $dh;
}

# Translates all of the C++ examples in the OpenSceneGraph examples folder into python
sub translate_all_examples {
    my $top_folder = shift;
    die unless opendir( my $dh, $top_folder);
    my $count = 0;
    while (readdir $dh) {
        my $example = $_;
        my $folder = "$examples_source_folder/$example";
        next unless -d $folder; # directories only, please
        next if $_ =~ m/^\./; # no hidden/special folders, please

        # Subset for testing
        $count += 1;
        # last if $count > 10; # Just a few for now while testing...
        # next unless $example =~ /manip/; # Just one for now while testing...

        print "Translating OSG example: ", $_, "\n";
        translate_example($example, $folder);
    }
    closedir $dh;
}

