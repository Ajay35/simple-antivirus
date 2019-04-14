from ftplib import FTP
import os
from datetime import datetime
from config import config
from config import banners

def update_virus_signatures():
    ftp = FTP(config['ftphost'])
    ftp.login(config['user'],config['password'])

    files = ftp.nlst()
    for file in files:
        print("Downloading..." + file)
        ftp.retrbinary("RETR " + file ,open(os.getcwd()+"/data/signatures/" + file, 'wb').write)
    ftp.close()
    print(banners['updated'])