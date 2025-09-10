import socket 
from termcolor import colored
import colorama
import argparse 
import os  
import random


colorama.init() 
banar = r""" 
  / ____|     | |   / ____|                   | |    
 | (___  _   _| |__| (___   ___  __ _ _ __ ___| |__  
  \___ \| | | | '_ \\___ \ / _ \/ _` | '__/ __| '_ \ 
  ____) | |_| | |_) |___) |  __/ (_| | | | (__| | | |
 |_____/ \__,_|_.__/_____/ \___|\__,_|_|  \___|_| |_|
\n"""


print(colored(banar , 'green'))


parser = argparse.ArgumentParser()
parser.add_argument("-d" , "--domain" , help= "domin name to search. for example: google.com " , required=True )
parser.add_argument('-l' , '--list' , help=f'subdomains list file path. for example: subdomainList.txt',  required=True)
parser.add_argument('-O' , "--out" , help= "csv file to save domain Names and thier IPs. for exampe: googleSubdomians.csv" )
parser.add_argument("-v" , "--verbose" , help= "another way to represent the subdomains also in fail case" , action="store_true")
args = parser.parse_args()




def getIpAddr(DomainName):

    ''''
    this function takes domain name as a input and returns IP address 
    if successfully collect ip and return None if it is false 
    '''
    try:
        IP = socket.gethostbyname(DomainName)
        return IP
    except socket.gaierror: 
        return None  

with open (args.list , 'r') as subDomiansList:
    for subDomain in subDomiansList.readlines() :
        subDomain = subDomain.strip()
        domian =f"{subDomain}.{args.domain}"
        IP = getIpAddr(domian)
        if IP != None :
            print(f"{colored("[+] FOUNDED:" , "green")} {domian:<20} {IP}") #formating like this 
        else:
            if args.verbose :   
                print(f"{colored("[+] NOTFOUND:" , 'red')} {domian:<20}")    
        if args.out:
            with open(args.out ,'a+') as outPutFile:
                if IP != None :
                    outPutFile.write(f"{colored("[+] FOUNDED:" , 'green')} {domian:<20} {IP}\n")
                else :
                    if args.verbose:
                        outPutFile.write(f"{colored("[+] NOTFOUND:" , 'red')} {domian:<20}\n")

                



    
    
    
    
    
