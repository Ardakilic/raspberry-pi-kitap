#!/bin/bash

#Arda Kilicdagi Not: Raspbian kurup ufaltmak yerine ben şahsen minibian kurmanızı tavsiye ederim:
#https://minibianpi.wordpress.com/

su
df -h
rm -rv python_games
rm -rv /opt/*
rm -rv /usr/share/icons/*
rm -rv /usr/games/
rm -rv /usr/share/squeak/
rm -rv /usr/share/sounds/
rm -rv /usr/share/wallpapers
rm -rv /usr/share/themes
rm -rv /usr/share/kde4
rm -rv /usr/share/images/*
apt-get autoremove -y x11-common
apt-get autoremove -y midori
apt-get autoremove -y omxplayer
apt-get autoremove -y scratch
apt-get autoremove -y dillo
apt-get autoremove -y xpdf
apt-get autoremove -y galculator
apt-get autoremove -y netsurf-common
apt-get autoremove -y netsurf-gtk
apt-get autoremove -y idle-python3.2
apt-get autoremove -y python*
apt-get autoremove -y lxde-common
apt-get autoremove -y lxde-icon-theme
apt-get autoremove -y lxdeterminal
apt-get autoremove -y hicolor-icon-theme 
apt-get autoremove â€“y
apt-get clean