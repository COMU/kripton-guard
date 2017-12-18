#!/usr/bin/python

import configparser, shutil, os, sys, getpass
from crontab import CronTab

currentDIR = os.path.dirname(os.path.realpath(__file__))
configDIR = "/etc/kripton-guard"
configFile = "/kripton-guard.conf"
user = getpass.getuser()
config=configparser.ConfigParser()

if os.getegid() != 0:
    sys.exit("Please run the script as root user!")

if not os.path.exists(configDIR):
    os.makedirs(configDIR)
    shutil.move(currentDIR + configFile,configDIR)

config.read(configDIR+configFile)
repeatTime=config['SETTINGS']['repeatTime']

my_cron = CronTab(user=user)
job = my_cron.new(command='python ' + currentDIR + '/kripton-guard.py')
job.minute.every(repeatTime)
my_cron.write()
