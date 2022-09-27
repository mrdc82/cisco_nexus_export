from netmiko import ConnectHandler
import paramiko
from getpass import getpass
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()
print('File loaded')

uusername = input("Username: ")
upassword = getpass()

nexus_list = []

with open(file_path) as file:
    for i in file:
        nexus_list.append(i.replace("\n", ""))

for i in nexus_list:
    cisco2 = {
        "device_type": "cisco_ios",
        "host": i,
        "username": uusername,
        "password": upassword,
    }

    # vpn-session command we execute to logoff user
    show_cmd = ['sh run', 'sh ver']
    #show_cmd = ['show ip route vrf all']

    try:
        with ConnectHandler(**cisco2) as net_connect:
            print("Gathering output for {}".format(i))
            #print("net_connect.find_prompt()")
            for j in show_cmd:
                sh_run_out = net_connect.send_command(j)
                with open("{}.cfg".format(i), "a") as out_file:
                    out_file.write(j+'\n'+sh_run_out)
    
        net_connect.disconnect()
    except ConnectionRefusedError as err:
        print(f"Connection Refused: {err}")
    except TimeoutError as err:
        print(f"Connection Refused: {err}")
    except Exception as err:
        print(f"Oops! {err}")

#END
