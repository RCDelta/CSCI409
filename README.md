# CSCI409
Semester Malware Project for Malware Analysis

# Overview
This project is going to be focusing on the MyDoom worm that broke out in 2004.

# Things I Know About the MyDoom
- It was usually deployed onto computers through email phishing, which was very easy to fall for in 2004
- Replaces a executable known as "taskmon.exe"
- Adds a DLL named "shimgapi.dll"
- Opens up TCP ports that are listening to execute files remotely
- There is a backdoor left open for future access. This left the ability for different types of cyber attacks to be conducted later
- Any email addresses found in the compromised systems are also sent phishing emails to spread the worm
- This attack has been sent specifically against the SCO Group and Microsoft. Minimal Damage in total against these two organizations.

# Things I Want to Replicate About MyDoom
- I would like to focus on how it engrains itself into a system (through a DLL/deep executable replacement) and how it spread faster than any other worm in the history of Cybersecurity.
- So far, I am focused on either Metasploit or Windows 11 for the target system
- I am going to make sure to isolate the target system to make sure that the spread will not affect the rest of the internet. I may create a spoofed website to try and DDOS or throw a remote shell for myself. I am not exactly sure how I want to affect the target.
- Also, one drawback is that many people do not keep contacts in the contacts folder, but back in the day, it was much more common.

# Conclusions
- I had a lot of trouble trying to inject into a necessary executable like "rundll32.exe"
- I completed the main part of the virus that I wanted, in that I read the contacts of anyone's folders and sent them a copy of the malware attached that uses my throwaway email to send it so that I may also have a copy of each email sent.
- The malware, when ran, tries to replace the rundll32.exe with a python file that is forced to become a executable to hide itself after the code is ran.
- Personally, I wish I could have done more to replicate it, but I think choosing Python was a mistake because it is too high level of a language to conduct such a complicated malware.
