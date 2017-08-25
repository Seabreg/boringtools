#!/usr/bin/perl

print "ADB Backup APK Extrator\nSoh pra facilitar minha vida\n\n";

my $x = `adb devices&>/dev/null`;
if ($x =~ m/List of devices attached/){
    
    print "[+] Devices Founds\n";
    my @b = split '\n', $x;

    foreach(@b[1,]){
        @device = split ' ', $_;
        @devics_id = @devices[0];
        print "[+] Id->".@device[0]."  | Model->".@device[4]."\n";
    }
    
    print "Device ID >>";
    my $id =  <STDIN>;
    chomp($id);
    
    my $packages = `adb -s $id shell pm list packages`;
    my $pkgs = $packages =~ s/:/--> /gr;
    
    print $pkgs;
    
    print "\nPackage Name ->";
    my $pkg = <STDIN>;
    chomp($pkg);
    
    my @path = split ":",`adb shell pm path $pkg`;
    print "[+] Path -> @path[1]";
    print "[*] Extraindo APK ..  ";
    my $extract = `adb pull @path[1]`;

}else{
    print "[-] Deu Ruim ";
}

