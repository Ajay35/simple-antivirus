import os
import sys
import ntpath
from threading import Thread
import algorithm
import utility
import docker_helper as dh

exelogpath="data/exelogs/"
txtlogpath="data/txtlogs/"

def main():
    arguments=sys.argv[1:]
    count = len(arguments)
    if count > 4 or count <4 :
        print ("Incorrect arguments")
        return 	
    if arguments[0]=='-o' and arguments[1] =='1':
        print("**********------------Signature based virus detection-------------************")
        print("\n")
        if arguments[2]=="-f":
            _,tail=ntpath.split(arguments[3])
            logpath=os.getcwd()+"/"+txtlogpath+tail+".txt"
            config = open("data/config","r").read().split("\n")
            utility.scanner(arguments[3],config,logpath)
        else:
            print("Incorrect Arguments")
            print("Usage:   python3 antivirus.py -o 1 -f filepath")            
         
    elif arguments[0] == "-o" and arguments[1]=="2":
        print("***********----------------Behaviour analysis-------------*********************")
        print("\n")
        if arguments[2]=="-f":
            if os.path.exists(arguments[3]):
                path=dh.generate_docker_file(arguments[3])
                cur_dir=os.getcwd()
                dh.build_image(path)
                _,tail = ntpath.split(arguments[3])
                print("filename:",tail)
                logpath=cur_dir+"/"+exelogpath+tail+".txt"
                dh.launch_image(path,logpath)
                os.chdir(cur_dir)
            else:
                print("File Not found")
        else:
            print("Incorrect Arguments")
            print("Usage:   python3 antivirus.py -o 1 -f filepath")


if __name__ == '__main__':
    main()
