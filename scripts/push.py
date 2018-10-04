#!/usr/bin/env python
import subprocess
import pushbullet
import keys

f = file = open('/var/www/html/log.txt', 'w+')
f.write(ip)
ip = subprocess.check_output(["hostname -I"], shell=True)
try:
	pb = pushbullet.Pushbullet(keys.PUSH)
	push = pb.push_sms(pb.devices[0], keys.PHONE, "EVE is online at http://" + ip)
	f.write("sending...\n")
except:
	print(keys.PUSH + " is incorrect...")
	f.write("send failled...\n")
f.write("done...\n")