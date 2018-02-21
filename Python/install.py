import configparser, shutil, os, sys, getpass
from crontab import CronTab

currentDIR = os.path.dirname(os.path.realpath(__file__))
configDIR = "/etc/kripton-guard"
configFile = "/kripton-guard.conf"
scriptDIR = "/opt/kripton-guard"
scriptFile = "/kripton-guard.py"
current_user = getpass.getuser()
config=configparser.ConfigParser()

if os.getegid() != 0:
    sys.exit("Please run the script as root user!")

if not os.path.exists(configDIR):
    os.makedirs(configDIR)
    shutil.move(currentDIR + configFile,configDIR)

if not os.path.exists(scriptDIR):
    os.makedirs(scriptDIR)
    shutil.move(currentDIR + scriptFile,scriptDIR)

config.read(configDIR+configFile)
repeatTime=config['SETTINGS']['repeatTime']

my_cron = CronTab(user=current_user)
job = my_cron.new(command='python ' + scriptDIR + '/kripton-guard.py')
job.minute.every(repeatTime)
my_cron.write()
