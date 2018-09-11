import requests
import time

def dirb():
    print("[+] Please Read README.MD First Necessary !  [+] ")
    url_in = input("Enter The Site To Search  ==> ")
    dir_dict = input("Enter Your Directory Dictionary List >> ")
    dir_dicts = open(dir_dict,'r').readlines()
    for items in dir_dicts:
        fu = items.strip()
        headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"}
        url = url_in+fu
        request = requests.get(url,headers=headers)
        http = request.content
        
        #if b'not found on this server' or b'Error 404 (Not Found)!!1' or b'Error 404' or b'Sh*t I Cant Find It' or b'Sorry ' or b'Not Found' or b'Ops File Not Found' or b'File Not Found On That Server' or b'doesn/t exists' or b'something went wrong':
            #print("File Not Found On The Server >> "+fu)
        if request.status_code >= 404 and b'404' or b'Not Found'  in http:
            print("File Not Found On The Server ==>  "+fu)
        else:
            print("File Has Been Found Successfully >> "+fu)
            fo = open('/home/hawkeye/Critical_File_Found.txt','a')
            fo.write(url)
            fo.close()
dirb()