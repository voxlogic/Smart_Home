#!/usr/bin/env python
#Davy Ragland | dragland@stanford.edu
#Home Automation System version 2.0 | 2016

#*********************************************************************
#                           SETUP
#*********************************************************************
import relayCGI

#*********************************************************************
#                            MAIN
#*********************************************************************
PIN_NUMBER = relayCGI.get_value("PIN_NUMBER")
relayCGI.set_mode(int(PIN_NUMBER))
if relayCGI.read_state(int(PIN_NUMBER)) == "1":
	relayCGI.relay_on(int(PIN_NUMBER))
else:
	relayCGI.relay_off(int(PIN_NUMBER))
relayCGI.blank_header()