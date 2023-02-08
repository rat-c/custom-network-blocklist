# custom network blocklist

A very basic configuration/blocklist to provide protection of phishing and malware in Europe (de-DE).

<img src="https://i.imgur.com/ah8GB08.png" height="150px"/>  

## What is a Blocklist?

Block lists are publicly maintained lists of domains, hosted on a web location somewhere.

## Usage

You can use the `blocklist.txt` for Pi-Hole by using the Web admin GUI > Settings > Blocklists.

## Automated fixing of wordlist

I have added a github action which sorts, removes duplicates and empty spaces from the wordlist, before re-commiting it with every push in the /main branch.

## Disclaimer
The files in this repository were created and modified by me for my own personal use and come with no guarantee to work for you. I provide these files "as-is" and offer no support whatsoever to get them working. It's always good to have multiple blocklists if you're relying heavily on those.
