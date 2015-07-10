#!/bin/env perl

use strict;
use warnings;

my $examples_source_folder = "F:/Users/cmbruns/build/OpenSceneGraph-3.2.1/OpenSceneGraph-3.2.1/examples";
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

    my $ident_rx = '\b[a-zA-Z_][a-zA-Z0-9_]*\b'; # identifiers
    my $type_rx = '\b[a-zA-Z_][a-zA-Z0-9_]*\b'; # type names
    my $funcarg_rx = '$type_rx\s+$ident_rx(?:\s*=\s*\S+)'; # one argument to a function
    my $funcargs_rx = '\(\s*(?:$funcarg_rx(?:\s*,\s*$funcarg_rx)*)?\s*\)'; # parentheses and arguments to a function

    while ( $file_block =~ m/($ident_rx)/mg ) {
        print $1, "\n";
    }

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
    $file_block =~ s/[{};]//g;

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

