#-*-coding:cp1254-*-

import socket

s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = "localhost"
port = 9123

#Socket oluşumu ; Host ve Portun belirlenmesi.

s.connect((host,port))

#Sockete, belirlenen host ve porta bağlantı kurulması.

f = open("hey.txt","r")

#Dosyayı "r" izniyle açımı.

l=f.read(1024)

#f değişkenindeki dosyayı 1024 byte kavramıyla okumak.

s.send(l)

#Sockete veriyi gönderme işlemi.

f.close()

#Dosya kapatımı.

print "veri gönderildi."
s.close()

#Socket kapatımı.
