# python 2.6 

import pdb
from ftplib import FTP
import socket
import os
import zipfile

# constants
FTP_DOMAIN = 'meta.eblib.com'
USERNAME = 'usmai'
PASSWORD = 'qdF1m6s1'

# connect and log in
print "\n ----\n ---- Connecting...\n ----"
try:
    ftp = FTP(FTP_DOMAIN)
except:
    print "\nConnection error! Check your hostname.\n"

try:
    ftp.login(user= USERNAME, passwd = PASSWORD)
except socket.error as e:
    print "\nConnection error! Check your username and password.\n"

# get the filenames
data = ftp.nlst()
# get the last file in the list b/c it is newest
filename = data[-1]

# download the file
with open(filename, "wb") as f: 
    ftp.retrbinary("RETR " + filename, f.write)
print "\n ----\n ---- File downloaded: " + filename + "\n ----"

# unzip the file
zip = zipfile.ZipFile(filename)
zip.extractall()
print "\n ----\n ---- File unzipped\n ----"

# format data 


# diff the files later to check if they match the sed command
