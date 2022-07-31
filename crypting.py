import getpass
import pyAesCrypt
import os
def enter_password(password):
    flag = 0
    while flag != 1:
        password = getpass.getpass(prompt = "Enter your password: ", stream = None)
        password_for_check = getpass.getpass(prompt = "Re-enter your password: ", stream = None)
        if password != password_for_check:
            print("Passwords not matching")
        else:
            print("[+] Password set up successfully")
            flag = 1
    if os.path.exists("/tmp/pass.txt") == False:
        file = open('/tmp/pass.txt','w')
    else:
        file = open('/tmp/pass.txt','a')
    file.write(password)
    file.write("\n")
    file.close()
    return password

def detect_our_non_crypted_files(filelist):
    path = os.getcwd()
    for root, dirs, files in os.walk(path):
        for file in files:
            if (file.endswith(".pdf")):
                filelist.append(os.path.join(root,file))
    return filelist

def encrypt(filelist,password):
    buffer_size =  1024 * 512
    for file in filelist:
        if os.path.exists(f"{file}"+".aes"):
            print(f"[?] File {file} already exists")
            os.remove(f"{file}"+".aes")
        pyAesCrypt.encryptFile(file,f"{file}"+".aes",password,buffer_size)
        print(f"[+] File {file} successfully encrypted")

def detect_our_crypted_files(filelist_crypt):
    path = os.getcwd()
    for root, dirs, files in os.walk(path):
        for file in files:
            if (file.endswith(".aes")):
                filelist_crypt.append(os.path.join(root,file))
    return filelist_crypt

def decrypt(filelist_crypt):
    buffer_size =  1024 * 512
    flag = 0
    all = 0
    count = 0
    while flag != 1:
        password = getpass.getpass(prompt = "Enter your password: ", stream = None)
        file_pswd = open("/tmp/pass.txt","r")
        for password_for_check in file_pswd:
            all +=1
            password_for_check = password_for_check.strip()
            if password == password_for_check:
                for file in filelist_crypt:
                    print(f"[+] File {file} successfully decrypting")
                    pyAesCrypt.decryptFile(f"{file}","decrypted_file.pdf",password,buffer_size)
                    print(f"[+] File {file} successfully decrypted")
                    flag = 1
                    break
            else:
                continue
            print("errors")
    file_pswd.close()

def main():
    password = ""
    filelist = []
    filelist_crypt = []
    flag = 0
    flag_1 = 0
    counter_operation = 0
    while flag != 1:
        ask_for_action = input("What do you want? Encrypt(e) or decrypt(d)?(e/d): ")
        if ask_for_action == "e":
            while flag_1 != 1:
                ask_for_encrypt = input("Do you want encrypt one(o) or all(a) files? o/a: ")
                if ask_for_encrypt =="a":
                    flag_1 = 1
                    detect_our_non_crypted_files(filelist)
                elif ask_for_encrypt == "o":
                    flag_1 = 1
                    path = input("Enter full path to file: ")
                    filelist.append(path)
            password = enter_password(password)
            encrypt(filelist,password)
            flag = 1

        elif ask_for_action == "d":
            while flag_1 != 1:
                ask_for_decrypt = input("Do you want decrypt one(o) or all(a) files?(o/a): ")
                if ask_for_decrypt =="a":
                    flag_1 = 1
                    detect_our_crypted_files(filelist_crypt)
                elif ask_for_decrypt == "o":
                    flag_1 = 1
                    path = input("Enter full path to file: ")
                    filelist_crypt.append(path)
            decrypt(filelist_crypt)
            flag = 1

        else:
            print("[!] Entered incorrect operation")
            counter_operation +=1
            if counter_operation != 0:
                ask_for_continue = input("Do you want exit?(y/n): ")
                if ask_for_continue == "n":
                    continue
                else:
                    exit(1)
if __name__ == "__main__":
    main()
