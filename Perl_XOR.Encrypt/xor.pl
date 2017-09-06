#!/usr/bin/perl

# XOR Encrypt Perl 

sub xorpl {
    my $string = shift;
    my $key = shift;
    my $boo = shift;
    my @crypt;
    foreach $chr(split //, $string){
        foreach $pass(split //, $key){
            if($boo == 1){
            push @crypt, $chr ^ $pass;
            }else{
            push @crypt, $pass ^ $chr;
            }
        }
    }
    return @crypt;

}

my $s = "Text to crypt in Xor";

# Encypting
my $x = join('',xorpl($s,"b",1));
print "Encryption String => ".$x;

# Decrypting
my $y = join('',xorpl($x,"b",0));
print "\n\nDecryption => ".$y."\n\n";
