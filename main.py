import os
import sys
import ntpath
from threading import Thread
import algorithm
import utility
import docker_helper as dh
import update
from config import config
from config import errors
from config import banners

exelogpath=config['exelogs']
txtlogpath=config['txtlogs']
signature_path=config['signatures_path']


def main():
    arguments=sys.argv[1:]
    count = len(arguments)
    if count > 4 or count <4 :
        print (errors['args'])
        return 	
    if arguments[0]=='-o' and arguments[1] =='1':
        print("\n")
        print(banners['headings_1'])
        print("\n")
        if arguments[2]=="-f":
            _,tail=ntpath.split(arguments[3])
            logpath=os.getcwd()+"/"+txtlogpath+tail+".txt"
            utility.scanner(arguments[3],signature_path,logpath)
        else:
            print(errors['args'])
            print(errors['Usage Error:1'])            
         
    elif arguments[0] == "-o" and arguments[1]=="2":
        print("\n")
        print(banners['headings_2'])
        print("\n")
        if arguments[2]=="-f":
            if os.path.exists(arguments[3]):
                path=dh.generate_docker_file(arguments[3])
                cur_dir=os.getcwd()
                dh.build_image(path)
                _,tail = ntpath.split(arguments[3])
                print("Filename:",tail)
                logpath=cur_dir+"/"+exelogpath+tail+".txt"
                dh.launch_image(path,logpath)
                os.chdir(cur_dir)
            else:
                print(errors['file_error'])
        else:
            print(errors['args'])
            print(errors['Usage Error:2'])
    


if __name__ == '__main__':
    main()


