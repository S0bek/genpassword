#!/usr/bin/perl -w
#
# Programme permettant de generer un mot de passe de la taille souhaitee, fournie en parametre
# Cree par S0bek
#
#
use strict;
use Term::ANSIColor;

#Fonctions principales
sub genpass ($);
sub enforce ($);

sub genpass ($) {
    my $length = shift;
    my $password = '';
    my @chars = ("a".."z" , "A".."Z" , 0..9 , '$' , '#' , '!' , '+');

    for (my $i = 0 ; $i < $length ; $i++) {
        my $rnd = int(rand(scalar(@chars)));
        $password .= $chars[$rnd];
    }
    return $password;
}

sub enforce ($) {
    my $pass = shift;
    my @spechar = ('$' , '#' , '!' , '+');
    my $pos = int(rand(scalar(@spechar)));
    my $rndchar = $spechar[$pos];
    my $passlen = int(length($pass));
    my $rndpos = int(rand($passlen));
    my @tmp = split(// , $pass);
    my @pwd;

    if ($pass !~ /(\$|\+|\#|\!)/g) {
        for (my $i = 0 ; $i < $passlen ; $i++) {
            if ($i == $rndpos) {
                $pwd[$i] = $rndchar;
            } else {
                $pwd[$i] = $tmp[$i];
            }
        }
    }
    $pass = join("" , @pwd) if (scalar(@pwd) > 0);
    return $pass;
}

#Verification de la saisie utilisateur
my $len = shift or die "Usage: $0 \[taille\]\n";
die "Usage: $0 \[taille\]\n" unless(scalar(@ARGV) == 0);
die "Il faut saisir un chiffre\n" unless ($len =~ /\d/);

#Generation du mot de passe en fonction de la taille choisie + renforcement du mot de passe si ce dernier ne contient aucun caractere special
my $pwd = genpass($len);
$pwd = enforce ($pwd);

print color 'bright_yellow';
print "$pwd\n";
print color 'reset';
