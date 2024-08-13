#!/bin/bash

#This script automates the updating and upgrading process

sep="-----------------------------"
wel="Thank you for using Kenzie's upgrade script"
exit="Please enjoy your newly upgraded OS!"
echo $wel
echo $sep
sudo pacman -Syu
echo $sep
sudo pacman -Sc
sudo $sep
sudo pacman -Qdtq | pacman -Rns -
echo $sep
echo "The script may not have detected all packages."
echo "Here is a list of packages that may still be useless"
pacman -Qqd | pacman -Rsu --print -
echo $exit
