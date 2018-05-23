# python 2.6 
from ftp_info import FTP_DOMAIN, USERNAME, PASSWORD
import pdb
from ftplib import FTP
import socket
import os
import zipfile
import csv
import re

# use pdb.set_trace() to break debugger

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

#get name of the extracted filenames and close
unzipped_files = zip.namelist()
zip.close()

print "\n ----\n ---- File unzipped\n ----"

# get dataloader files ready for writing
add_dataloader = open("usmai-active.txt", "w")
delete_dataloader = open("usmai-inactive.txt", "w")

# transform CSVs into dataloader filenames
for i, file in enumerate(unzipped_files):
    f = open(unzipped_files[i])
    # read CSV
    csv_f = csv.reader(f)
    # skip first line
    next(csv_f, None)
            
    # get data out of rows
    # get only numbers from the eisbn field
    def get_eisbn(row):
        return re.sub("\D", "", row[3]) 
    # get bkey
    def get_bkey(row):
        return row[0]
    
    # check to see if the file is to Add or Delete and give it an ACTIVE or INACTIVE status  
    def get_status(unzipped_file):
        if unzipped_files[i].endswith("Add.csv"):
            return status = "ACTIVE"
        elif unzipped_files[i].endswith("Delete.csv"):
            return status = "INACTIVE"
        else
            print "There is no Add.csv or Delete.csv. Could not generate txt file."
    
    # set the status INACTIVE or ACTIVE
    get_status(unzipped_files)
    
    
    # write to dataloader based on get_status
    def write_data(status):
    if unzipped_files[i].endswith("Add.csv"):
        for row in csv_f:
            eisbn = get_eisbn(row)
            bkey = get_bkey(row)
            add_dataloader.write(eisbn + "\tbkey=" + bkey +"\tACTIVE\n")
    elif unzipped_files[i].endswith("Delete.csv"):
        for row in csv_f:
            eisbn = get_eisbn(row)
            bkey = get_bkey(row)
            delete_dataloader.write(eisbn + "\tbkey=" + bkey +"\tINACTIVE\n")

            

            
            
            
    
            
        
        
        
        
        
    
    
    
    



# diff the files later to check if they match the sed command
