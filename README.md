# custom network blocklist

A very basic configuration/blocklist to provide protection of phishing and malware in Europe (de-DE).

<img src="https://i.imgur.com/ah8GB08.png" height="150px"/>  

## What is a Blocklist?

Block lists are publicly maintained lists of domains, hosted on a web location somewhere.

## Usage

You can use the `blocklist.txt` for Pi-Hole by using the Web admin GUI > Settings > Blocklists.

## Remove Duplicates

The `remove-duplicate.py` script allows quick removal of potential duplicates after adding those to the `blocklist.txt` The script works by reading the entire file into memory (stored as a list of lines), and then writing it back to the file, only including lines that haven't been seen before.

## Disclaimer
The files in this repository were created and modified by me for my own personal use and come with no guarantee to work for you. I provide these files "as-is" and offer no support whatsoever to get them working. It's always good to have multiple blocklists if you're relying heavily on those.
