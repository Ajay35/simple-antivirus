from ftplib import FTP
import os
from datetime import datetime


def update_virus_signatures():
    ftp = FTP('127.0.0.1')
    ftp.login('ajay','ajay35')

    files = ftp.nlst()
    for file in files:
        print("Downloading..." + file)
        ftp.retrbinary("RETR " + file ,open(os.getcwd()+"/data/signatures/" + file, 'wb').write)
    ftp.close()
    print('Signature database updated.')