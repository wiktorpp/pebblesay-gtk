#!/bin/bash
echo "-> nishisay test test test..."
nishisay test test test test test test test test test test test test test test test test

echo "-> cat loremIpsum.txt | nishisay -n"
cat loremIpsum.txt | nishisay -n

echo "-> figlet test | nishisay"
figlet test | nishisay

echo "-> nishisay -c XD"
nishisay -c XD
echo "-> nishisay -nt \"Hi, \\nhow are you? AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\""
nishisay -nt "Hi, \nhow are you? AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

echo "-> nishisay"
nishisay

echo "-> nishisay -t"
nishisay -t

echo "-> nishisay -p"
nishisay -p
