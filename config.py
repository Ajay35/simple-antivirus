config = {
    'signatures_path': 'data/signatures/',
    'exelogs': 'data/exelogs/',
    'txtlogs': 'data/txtlogs/',
    'ftphost':'127.0.0.1',
    'user':'ajay',
    'password':'ajay35',
    'source':'/home/ajay/ftp',
    'destination':'data/signatures/'
}

errors={
    'file_error':'File Not found',
    'args':'Incorrect Arguments',
    'Usage Error:1': 'Usage:   python3 antivirus.py -o 1 -f txtfilepath',
    'Usage Error:2': 'Usage:   python3 antivirus.py -o 2 -f jarfilepath'
}

banners={
    'headings_1': '**********------------Signature based virus detection-------------************',
    'headings_2':'***********----------------Behaviour analysis-------------*********************',
    'updated':'Signature database updated.',
    'input_alert':'What do you want to do with the infected file?\n[a] Remove file\n[b] Nothing\n[c] Add in Quanrantine list \nSelection:',
    'update_alert':"Would you like to update the anti-virus for more security?\n[a] Yes\n[b] No\nSelection: ",
    'thank_you':'Thank you for using antivirus.',
    'alert_msg':'Be Careful.File might harm your computer data' 
}
docker_commands={
    'build_image':'sudo docker build -t test . > /dev/null',
    'launch_image':'sudo docker run -d --rm --name test_container test >> /dev/null',
    'stats_image':'sudo docker stats --no-stream test_container',
    'stop_image':'sudo docker stop test_container > /dev/null'
}