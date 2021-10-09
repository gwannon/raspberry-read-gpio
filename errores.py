#!/usr/bin/env python
# encoding: utf-8

from time import sleep
import RPi.GPIO as GPIO
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
 
GPIO.setmode(GPIO.BCM)

INPUT_PIN1 = 4
GPIO.setup(INPUT_PIN1, GPIO.IN)	# Establecemos que podemos leer del GPIO 4

INPUT_PIN2 = 17
GPIO.setup(INPUT_PIN2, GPIO.IN)	# Establecemos que podemos leer del GPIO 17

def send_mail( puertoGPIO ):
	smtp_ssl_host = 'smtp.xxxxxxx,com'  		# smtp.micorreo.com
	smtp_ssl_port = 465				# puerto
	username = 'sender@mail.com'			# usuario para identificar
	password = 'xxxxxxxx'				# contraseña para identificar
	sender = 'sender@mail.com'			# email para el from del email
	targets = ['reciever@mail.com']		# emails a los que se enviará correos
	
	now = datetime.now()
	msg = MIMEText(now.strftime("%d/%m/%Y %H:%M:%S")+' ERROR PUERTO GPIO ' + puertoGPIO)
	msg['Subject'] = 'ERROR GPIO' + puertoGPIO
	msg['From'] = sender
	msg['To'] = ', '.join(targets)

	server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
	server.login(username, password)
	server.sendmail(sender, targets, msg.as_string())
	server.quit()
	return


while True: # Empezamos bucle infinito
	if (GPIO.input(INPUT_PIN1) == True): # Leemos el Pin 4
		#now = datetime.now()
		#print now.strftime("%d/%m/%Y %H:%M:%S") + ' Enviar correo ERROR GPIO 4'
		send_mail("4") # enviamos el email
		sleep(5) # Paramos durante 5 segundos para que el automata pueda dejar de  pulsar el pin y no mandar varios mails seguidos
	elif (GPIO.input(INPUT_PIN2) == True): # Leemos el Pin 17
		#now = datetime.now()
		#print now.strftime("%d/%m/%Y %H:%M:%S") + ' Enviar correo ERROR GPIO 17'
		send_mail("17")
		sleep(5) # Paramos durante 5 segundos para que el automata pueda dejar de  pulsar el pin y no mandar varios mails seguidos
	else:
		#now = datetime.now()
		#print now.strftime("%d/%m/%Y %H:%M:%S") + ' NADA'
		sleep(0.1); # Paramos durante 0,1 segundos




