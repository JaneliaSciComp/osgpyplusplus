#!/bin/env perl

use strict;
use warnings;

my $examples_source_folder = "F:/Users/cmbruns/build/OpenSceneGraph-3.2.1/OpenSceneGraph-3.2.1/examples";
translate_all_examples($examples_source_folder);

sub translate_all_examples {
    my $top_folder = shift;
    die unless opendir( my $dh, $top_folder);
    while (readdir $dh) {
        my $folder = "$examples_source_folder/$_";
        next unless -d $folder; # directories only, please
        next if $_ =~ m/^\./; # no hidden/special folders, please
        print $_, "\n";
    }
    closedir $dh;
}

