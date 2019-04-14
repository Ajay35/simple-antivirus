import os
import sys
import re
import algorithm
import docker_helper as dh
import update
from config import config
from config import errors
from config import banners


def resource_log(cpu,mem,logpath):

    with open(logpath,'w+') as logfile:
        if cpu > 80 or mem >35:
            logfile.write("Virus : Found")
        else:
            logfile.write("Virus : Not Found")
        logfile.write("\n")
        logfile.write("CPU Usage (%) : ")
        logfile.write(str(cpu))
        logfile.write("\n")
        logfile.write("Memory Usage : ")
        logfile.write(str(mem))
        logfile.write("\n")
    print("Log saved at data/exelogs")
    choice=input(banners['update_alert'])
    if choice == "a":
        print("Updating antivirus")
        update.update_virus_signatures()
    elif choice=="b":
        print (banners['thank_you'])
    print("--------------------")
    
    

def process_output(s,logpath):
    string_arr=s.split(" ")
    literals_list=[]
    for i in string_arr:
        if len(i)>0:
            literals_list.append(i)
    cpu_per=""
    mem_use=""
    cpu=re.findall("\d+",literals_list[17])
    mem=re.findall("\d+",literals_list[18])
    
    
    if len(cpu)==2:
        cpu_per+=cpu[0]+"."+cpu[1]
    else:
        cpu_per+=cpu[0]
    
    if len(mem)==2:
        mem_use+=mem[0]+"."+mem[1]
    else:
        mem_use+=mem[0]


    print("CPU Usage:",float(cpu_per))
    print("Memory Usage:",float(mem_use))
    print("\n")
    if float(cpu_per)> 80.0 or float(mem_use)>35:
        print('\033[91m' + "[High Resource Usage Deetected :Virus Found]")
    else:
        print ('\033[92m' + "No Virus Found [Clean]")
    
    return resource_log(float(cpu_per),float(mem_use),logpath)



def add_to_quarantine(filename):
    # idle function
    print(filename)
    with open("test.txt", "a") as myfile:
        print("added to quarantine")
        myfile.write("demo")



def log_writer(logpath,virusnames):
    output= open(logpath,"w+")
    if len(virusnames)==0:
        output.write("Virus : Not Found")
        output.write("\n")
        output.write("Names of Virus Signatures Found : ")
        output.write("\n")
    else:
        output.write("Virus : Found")
        output.write("\n")
        output.write("Names of Virus Signatures Found : ")
        output.write("\n")
    for i in virusnames:
        output.write(i)
        output.write("\n")
    print("Log written at data/txtlogs ")
    print("---------------------------------------")
    output.close()
    choice=input(banners['update_alert'])
    if choice == "a":
        print("Updating antivirus")
        update.update_virus_signatures()
    elif choice=="b":
        print (banners['thank_you'])
        print("--------------------")

def scanner(filename,virussignpath,logpath):

    exists = os.path.exists(filename)
    is_file=os.path.isfile(filename)
    if exists is False:
        print(errors['file_error'])
        return -1
    file_text=''
    if is_file is True:
        with open(filename,'r') as file:
            file_text= file.read()

    flag=False
    virusnames=[]
    if os.path.isdir(filename) == False:
        print("File scanning")
        for virus_signature_file in os.listdir(virussignpath):
            viruspath=virussignpath+"/"+virus_signature_file
            with open(viruspath,'r') as file:
                signature = file.read()
                found=algorithm.KMPSearch(signature,file_text)
                if found:
                    flag=True
                    print('\033[91m' + "[Infected by %s]" % virus_signature_file)        
                    virusnames.append(virus_signature_file.split('.')[0])
        if flag is False:
            print ('\033[92m' + "No Virus Found [Clean]")
        else:
            choice=input(banners['input_alert'])
            if choice == "a":
                os.remove(filename)
                print("File successfully removed!")
            elif choice=="b":
                print ("Be Careful.This file might harm your computer data")
                #add_to_quarantine(filename)
        log_writer(logpath,virusnames)

    else:
        print("Directory Scanning")
        for single_file in os.listdir(filename):
            print(single_file)
            for virus_signature_file in os.listdir(virussignpath):
                viruspath=virussignpath+"/"+virus_signature_file
                with open(viruspath,'r') as file:
                    signature = file.read()
                filepath=filename+"/"+single_file
                with open(filepath,'r') as inputfile:
                    file_text=inputfile.read()
                    found=algorithm.KMPSearch(signature,file_text)
                    if found:
                        flag=True
                        print('\033[91m' + "[Infected by %s]" % virus_signature_file)        
                        virusnames.append(virus_signature_file.split('.')[0])
            if flag is False:
                print ('\033[92m' + "No Virus Found [Clean] in ",single_file)
            else:
                choice=input(banners['input_alert'])
                if choice == "a":
                    os.remove(filename+"/"+single_file)
                    print("File successfully removed!")
                elif choice=="b":
                    print (banners['alert_msg'])
                elif choice=="c":
                    print("Add in quarantine")
            log_writer(single_file,virusnames)
            virusnames.clear()
            flag=False
