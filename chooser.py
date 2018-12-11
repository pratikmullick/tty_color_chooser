import json
import subprocess
import os,sys

def create_config(color_data,config_file):
    with open (color_data,"r") as data_file:
        data = data_file.readlines()
        ctr = 1
    for line in data:
        c_data = json.loads(line)
        for name,c_vals in c_data.items():
            print(str(ctr)+". "+name)
            ctr += 1
    colset_value = int(input("Choose color set: "))
    col_set = json.loads(data[colset_value - 1])

    with open(config_file,"w") as shellfile:
        shellfile.write("#!/bin/bash\n")
        for name,dataset in col_set.items():
            for val,c_vals in dataset.items():
                shellfile.write("echo -en \"\e]P"+val+c_vals+"\"\n")
        shellfile.write("clear\n")

def run_config(config_file):
    subprocess.Popen(["chmod","+x",config_file])
    exec_line = "./"+config_file
    subprocess.Popen([exec_line])
    sys.exit(0)
                
def delete_config(config_file,state):
    if state == 1:
        del_yn = input("Delete File (Y / N)? ")
        del_yn = del_yn.lower()
        if del_yn == "y":
            subprocess.Popen(["rm", config_file])
            print("Color Configuration file deleted.")
        sys.exit(0)
    else:
        subprocess.Popen(["rm", config_file])

def main():
    color_data = "color.json"
    config_file = "tty_color.sh"
    if os.path.exists(config_file):
        print("A previous configuration file exists.")
        action = int(input("1. New\n2. Delete\n3. Install\n4. Exit\n? "))
        if action == 1:
            delete_config(config_file,0)
            create_config(color_data, config_file)
            run_ask = input("Install new color configuration? (Y / N): ")
            run_ask = run_ask.lower()
            if run_ask == "y":
                run_config(config_file)
            else:
                sys.exit(0)
        elif action == 2:
            delete_config(config_file,1)
        elif action == 3:
            run_config(config_file)
        elif action == 4:
            sys.exit(0)
        else:
            print ("Choose correct option!")
    else:
        choice = input("Create a new color configuration? (Y / N): ")
        choice = choice.lower()
        if choice == "y":
            create_config(color_data, config_file)
            run_ask = input("Install new color configuration? (Y / N): ")
            run_ask = run_ask.lower()
            if run_ask == "y":
                run_config(config_file)
        else:
            sys.exit(0)

while True:
    main()
