#!/bin/env perl

use strict;
use warnings;

my $examples_source_folder = 
    # "F:/Users/cmbruns/build/OpenSceneGraph-3.2.1/OpenSceneGraph-3.2.1/examples";
    "C:/Users/cmbruns/git/osg/examples";
translate_all_examples($examples_source_folder);

# Translates one C++ source file into python
sub translate_source_file {
    my $file = shift;
    die unless open( my $fh, $file );
    my $file_block = join("", <$fh>); # Read entire file at once

    # TODO: translate code

    # Parse osg modules used, from headers
    # #include <osg/ApplicationUsage>
    my %modules = ();
    while ( $file_block =~ m/^#include\s+[<"](\w+)\//mg ) {
        $modules{$1} += 1;
    }
    while (my ($mod, $count) = each %modules ) {
        print $mod, ": ", $count, "\n";
    }

    # Regexes can only do finite nesting of parentheses
    my $paren_rx = "\\([^()]*\\)";
    my $paren2_rx = "\\((?:[^()]*${paren_rx})*[^()]*\\)";
    my $paren3_rx = "\\((?:[^()]*${paren2_rx})*[^()]*\\)";
    my $paren4_rx = "\\(((?:[^()]*${paren3_rx})*[^()]*)\\)"; # capture insides

    # Regular expressions to help (mostly) identify function declarations
    my $ident_rx = "[a-zA-Z_][a-zA-Z0-9_]*"; # identifiers
    my $type_rx = "(?:const\\s+)?(?:$ident_rx\\:\\:)*$ident_rx(?:\\s*\\*+|&)?"; # type names
    my $arg_ident_rx = "(?:\\*+|&)?($ident_rx)"; # e.g. "**argv"
    my $funcarg_rx = "$type_rx\\s+$arg_ident_rx(\\s*=\\s*\\S+)?"; # one argument to a function
    my $funcargs_rx = "\\(\\s*($funcarg_rx(?:\\s*,\\s*$funcarg_rx)*)?\\s*\\)"; # parentheses and arguments to a function
    my $func_rx = "^(\\s*)$type_rx\\s+($ident_rx)\\s*$funcargs_rx\\s*{\\s*\$\\n";

    # Translate function declarations
    while ( $file_block =~ m/($func_rx)/mg ) {
        my $cpp_func = $1;
        my $indent = $2;
        my $fn_name = $3;
        my $all_args = $4;
        my @args = split ",", $all_args;
        my @arg_names = ();
        foreach my $arg (split ",", $all_args) {
            $arg =~ m/^\s*$funcarg_rx\s*$/;
            my $arg_name = $1;
            # my $equals = $2;
            # print $1, "\n"
            push @arg_names, $1;
        }
        my $py_func = "${indent}def $fn_name(";
        $py_func .= join ", ", @arg_names;
        $py_func .= "):\n";

        # print $cpp_func, "\n";
        # print $py_func;
        $file_block =~ s/\Q${cpp_func}/${py_func}/;
    }

    my $dec_ass_rx = "(^([\\t\ ]*)$type_rx\\s+$arg_ident_rx\\s*=([^;]*);)";

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
    my $dec_init_rx0 = "^([\\t\ ]*)($type_rx)\\s+($arg_ident_rx)\\s*\\s*;";
    while ( $file_block =~ m/($dec_init_rx0)/mg) {
        my $cpp_dec = $1;
        my $indent = $2;
        my $type = $3;
        my $ident = $4;
        # We will remove the semicolon later
        my $py_dec = "$indent$ident = $type();";
        # print $cpp_dec, "\n";
        # print $py_dec, "\n";
        $file_block =~ s/\Q${cpp_dec}/${py_dec}/;
    }

    # Declare and initialize "Bar foo(3);"
    my $dec_init_rx = "^([\\t\ ]*)($type_rx)\\s+($arg_ident_rx)\\s*($paren4_rx)\\s*;";
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

    my $ifwhile_rx = "(if|while)\\s*$paren4_rx";
    while ( $file_block =~ m/($ifwhile_rx)/mg) {
        my $cpp_while = $1;
        # strip one set of parentheses
        my $kw = $2;
        my $contents = $3;
        my $py_while = "$2 $3 :";
        # print $cpp_while, "\n";
        # print $py_while, "\n";
        $file_block =~ s/\Q${cpp_while}/${py_while}/;
    }

    $file_block =~ s/\belse\b/else:/g;


    # Translate console output statements
    $file_block =~ s/(?:std::)?cout\s*<<\s*/print /g;
    $file_block =~ s/\s*<<\s*(?:std::)?endl//g;
    $file_block =~ s/\s*<<\s*/, /g;

    # Translate string classes
    $file_block =~ s/std::string/str/g;

    # Convert comments from "//" and "/* */" to "#"
    $file_block =~ s!//!#!g;
    $file_block =~ s!/\*!#!g;
    $file_block =~ s!\*/!!g;

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

    return $file_block, \%modules;
}

# Translates one OpenSceneGraph example folder from C++ to python
sub translate_example {
    my $example = shift;
    my $folder = shift;
    die unless opendir( my $dh, $folder);
    while (readdir $dh) {
        my $file = "$folder/$_";
        next unless -f $file; # Files only, please
        next unless $_ =~ m/\.[ch]/; # C++ source files only, please
        print "  Translating source file: ", $_, "\n";
        my ($source_block, $modules) = translate_source_file($file);
        die unless open( my $pyfh, ">$example.py" );
        print $pyfh $source_block;
        close($pyfh);
    }
    closedir $dh;
}

# Translates all of the C++ examples in the OpenSceneGraph examples folder into python
sub translate_all_examples {
    my $top_folder = shift;
    die unless opendir( my $dh, $top_folder);
    while (readdir $dh) {
        my $example = $_;
        my $folder = "$examples_source_folder/$example";
        next unless -d $folder; # directories only, please
        next if $_ =~ m/^\./; # no hidden/special folders, please
        print "Translating OSG example: ", $_, "\n";
        translate_example($example, $folder);
        last; # Just one for now while testing...
    }
    closedir $dh;
}

