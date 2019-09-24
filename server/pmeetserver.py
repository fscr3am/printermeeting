  #-*-coding:cp1254-*-
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = "localhost"
port = 9123

#Socket oluşumu ; host ve port belirlenimi.

s.bind((host,port))

#Host ve Port oluşumu.

f = open("alindi.txt","a")

#Dosyayı "a" izniyle açmak.

s.listen(15)

#15 kişiye bağlantı izni vermek.

server,addr = s.accept()

#bağlantı kabulü.

print "bağlantı kuruldu :", addr

while True:
    
    l = server.recv(1024)
# L değişkenine karşı taraftan alınan veriyi ekliyoruz.
    print "alınıyor..."
    f.write(l)
    f.write("\n")
    f.write("\n")
    f.close()
#Dosya kapatılır.
    print "veri alındı."
    server.close()
#Bağlantı kapatılır.
    exit()
