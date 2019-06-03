#!/usr/bin/python
import requests, sys
from bs4 import BeautifulSoup as bfs
from subprocess import run, DEVNULL, check_output
from os.path import isdir

if len(sys.argv) != 2:
    print("Usage: aaurh somepackagename")
    exit()

search = sys.argv[1]
results = []

r = requests.get("https://aur.archlinux.org/packages/?O=0&K=" + search)
s = bfs(r.text, 'html.parser')
table = s.find('table', {'class':'results'})
body = table.find('tbody')
r = body.find_all('tr')
n = 1
for i in r:
    name = i.find('a').contents[0]
    desc = i.find_all('td')[4].contents[0]
    results.append((name, desc))
    print("   "+str(n)+". "+name+": "+desc)
    n +=1
print("\n")
n = int(input("Select package by number:"))
selected = results[n-1][0]
homedir = check_output("echo ~", shell=True).decode('utf-8').replace("\n", "")
if isdir(homedir+"/aur") == False:
    print("~/aur is not yet there, creating it for you")
    cmd = "mkdir ~/aur"
    run(cmd, shell=True)
print("Cloning "+selected+" into ~/aur/"+selected)
cmd = "git clone https://aur.archlinux.org/"+selected+".git ~/aur/"+selected+"/"
run(cmd, shell=True, stdout=DEVNULL, stderr=DEVNULL)
i = input("Would you like to view the PKGBUILD? [y,n]")
if i == "y":
    cmd = "nano ~/aur/"+selected+"/PKGBUILD"
    run(cmd, shell=True)
i = input('Would you like to run "makepkg -si" now? ' + (
    "WARNING: You have not yet viewed the PKGBUILD file. Do not install anything you don't trust! " if i != "y" else ""
) +  ' [y,n]')
if i == "y":
    cmd = "cd ~/aur/"+selected+" && makepkg -si"
    run(cmd, shell=True)
