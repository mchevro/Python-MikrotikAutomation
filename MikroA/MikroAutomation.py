'''
AUTHOR    : MCHEVRO
PYTHON    : 3.8
Github    : https://github.com/mchevro
Refrensi  : https://github.com/ArRosid
'''
import paramiko 
import time
from getpass import getpass
import sys
import os

print("MIKROTIK AUTOMATION\n")
try:
    while True:
        try:
            input_file  = input("Masukan File IP          : ")              #Masukan File Yang Berisi IP Router
            baca_file   = open(input_file, "r").readlines()                 #Membaca File IP Yang Sudah Dimasukan  
            break
        except:
            print("File Tidak Ada!")                                        #Jika Nama File Tidak Ada Maka Akan Muncul Output Ini
            continue

    ip_list      = []                                                       #Membuat List Berisi IP Router
    for x in baca_file:
        ip_list.append(x.strip())

    while True:
         try:
            input_config = input("Masukan File Konfigurasi : ")             #Memasukan File Yang Berisi Konfigurasi CLI Mikrotik
            baca_config = open(input_config, "r").readlines()               #Membaca File Konfigurasi Yang Sudah Dimasukan
            break
         except:
            print("File Tidak Ada!")                                        #Jika Nama File Konfigurasi Tidak Ada Maka Akan Muncul Output Ini
            continue
        
    username = input("\nMasukan Username  : ")                              #Memasukan Username Login SSH Router
    password = getpass("Masukan Password  : ")                              #Memasukan Password Login SSH Router

    for ip in ip_list:                                                      #Mengambil List IP Yang Ada Di File IP Router Untuk Login Ke SSH
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(
            hostname=ip,
            port=9090,                                                      #Isi Dengan Port SSH.. Contoh port=9090
            username=username,
            password=password)
        print ("\nBerhasil Login {}".format(ip))                            #Jika Berhasil Masuk Maka Akan Muncul output Ini

        try:                                                                #Mecoba Konfigurasi Mikrotik
            for config in baca_config:
                ssh_client.exec_command(config)
                time.sleep(1)
            print("Konfigurasi Sukses {}".format(ip))
        except:
            print("failed")

    print("\nSelesai\n")                                                    #Output Selesai Konfigurasi 

except KeyboardInterrupt:
    print("\nKeluar Dari Pengaturan\n")                                     #Keluar Dari Pengaturan Oleh User
    sys.exit()