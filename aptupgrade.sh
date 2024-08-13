#!/bin/bash

#This script automates the updating and upgrading process

sep="---------------------"
echo $sep
echo "Upgrade list"
sudo apt list --upgradable
echo $sep
sudo apt update
sudo apt upgrade
echo $sep
sudo apt autoremove
echo "Enjoy :3"
