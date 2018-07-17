#!/usr/bin/perl
@songs = `curl https://krasfs.ru/music/muzlo.php?muzlo=House-Russian -k` =~ m/mp3: \"(\S.+)\"/g;
foreach(@songs){print `wget "$_" --no-check-certificate`;}