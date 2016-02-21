#!/usr/bin/env python
# Author: Matthew Feickert
# Date: 2016-02-21
# Python script to update GitHub's Atom text editor to the latest version

import sys
import subprocess

if (sys.version_info > (3, 0)):
    # Python 3 code
    import urllib.request

    INSTALLED = subprocess.getoutput('atom --version')[:5]
    URL = "https://github.com/atom/atom/releases/latest"
    LATEST = urllib.request.urlopen(URL).geturl()[-5:]

    if (INSTALLED == LATEST):
        print("Your version of Atom (v{}) is up to date!".format(INSTALLED))
    else:
        print("Your version of Atom is v{}".format(INSTALLED))
        print("There is an updated version of Atom available: v{}".format(LATEST))
        CHOICE = input("Would you like to update Atom? [Y/n]")
        if (CHOICE == 'Y'):
            print("Updating Atom")
            subprocess.call(['wget', '-O', 'atom-amd64.deb',
                             'https://atom.io/download/deb'])
            subprocess.call(['sudo', 'dpkg', '-i', 'atom-amd64.deb'])
            subprocess.call(['rm', 'atom-amd64.deb'])
            INSTALLED = subprocess.getoutput('atom --version')[:5]
            print("Atom has been updated to v{}".format(INSTALLED))
        else:
            print("Exiting")
else:
    # Python 2 code
    import urllib2

    INSTALLED = subprocess.check_output(['atom', '--version'])[:5]
    URL = "https://github.com/atom/atom/releases/latest"
    LATEST = urllib2.urlopen(URL).geturl()[-5:]

    if (INSTALLED == LATEST):
        print("Your version of Atom (v{}) is up to date!".format(INSTALLED))
    else:
        print("Your version of Atom is v{}".format(INSTALLED))
        print("There is an updated version of Atom available: v{}".format(LATEST))
        CHOICE = raw_input("Would you like to update Atom? [Y/n]")
        if (CHOICE == 'Y'):
            print("Updating Atom")
            subprocess.call(['wget', '-O', 'atom-amd64.deb',
                             'https://atom.io/download/deb'])
            subprocess.call(['sudo', 'dpkg', '-i', 'atom-amd64.deb'])
            subprocess.call(['rm', 'atom-amd64.deb'])
            INSTALLED = subprocess.check_output(['atom', '--version'])[:5]
            print("Atom has been updated to v{}".format(INSTALLED))
        else:
            print("Exiting")
