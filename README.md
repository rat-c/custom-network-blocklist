# custom network blocklist

A very basic configuration/blocklist to provide protection of phishing and malware in Europe (de-DE).

<img src="https://i.imgur.com/ah8GB08.png" height="50px"/>

## What is a Blocklist?

A blocklist is a publicly maintained list of domains that are hosted on a web location and can be used to block access to them.

### The Importance of Finding the Right Balance

While there are many blocklists available, it's important to find the right balance between increased privacy and good functionality. Using every blocklist you come across may seem like a good idea, but this "nuke everything" approach can actually hinder your online experience.

### The Custom Network Blocklist

My custom network blocklist is designed to provide basic protection against phishing and malware attacks in Europe (de-DE), based on real-life cases that we have encountered in our daily operations as a Security Operations Center (SOC).

## Usage

### uBlock Origin

To set the blocklist in uBlock Origin, you will have to open up the settings, filter lists and scroll all the way down. There, you will have to insert the raw file, which will be confirmed by displaying 'X used out of X'. This should also sync from device to device, if setup correctly.

<img src="https://i.imgur.com/micR75O.png" height="250px"/>

### Others

You can use the `blocklist.txt` for Pi-Hole by using the Web admin GUI. Add the URL to your blocklists (Login > Group Management > Adlists > Paste list URL in "Address" field, add comment > Click "Add"). Then, update gravity (Tools > Update Gravity > Click "Update").

For AdGuard, you can add it to the block list by using the menu: Login > Filters > DNS Blocklists > Add blocklist > Add a custom list > Enter Name > Paste copied link URL. The list is then  automatically enabled and ready to start blocking.

## Issues, Add and Remove Requests

Please use the issues and the templates for these things.

## Automated fixing of wordlist

I have added a github action which sorts, removes duplicates and empty spaces from the wordlist, before re-commiting it with every push in the /main branch.

## Disclaimer
The files in this repository were created and modified by me for my own personal use and come with no guarantee to work for you. I provide these files "as-is" and offer no support whatsoever to get them working. It's always good to have multiple blocklists if you're relying heavily on those.
