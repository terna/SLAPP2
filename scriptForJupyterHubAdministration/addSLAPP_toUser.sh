#!/bin/bash

sudo cp -R SLAPP /home/$1/
sudo cp README.1ST /home/$1/
sudo chown -R $1:$1 /home/$1/SLAPP
