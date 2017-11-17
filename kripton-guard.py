#!/usr/bin/python

#LAN Scanner

from scapy.all import *
import configparser
import sqlite3

conn = sqlite3.connect('network.db')

config=configparser.ConfigParser()
config.read('kripton-guard.conf')
subnet=config['SETTINGS']['subnet']
interface=config['SETTINGS']['interface']

def createTables(conn):
    #Create db table if it's not exist
    conn.execute("CREATE TABLE mac_ip_addresses (ID INTEGER PRIMARY KEY AUTOINCREMENT, macAddress varchar(17) UNIQUE NOT NULL, ipAddress varchar(15) NOT NULL, comment varchar(50) )")

def showDevices():
    #Shows devices in whitelist
    print "\n========== Your Devices ==========\n    Mac Address       IP Address   "
    query = "SELECT macAddress,ipAddress FROM mac_ip_addresses;"
    result = conn.execute(query)
    for row in result:
        print row[0] + "    " + row[1] + "\n"
    print "==================================="

ans,unans=srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=subnet), timeout=5, iface=str(interface))

if(config['SETTINGS']['firstTime']=='1'):
    config['SETTINGS']['firstTime']='0'
    with open('kripton-guard.conf','w') as configfile:
        config.write(configfile)
    createTables(conn)
    for s,r in ans:
        mac=(r.sprintf("%Ether.src%"))
        ip=(r.sprintf("%ARP.psrc%"))
        query= "INSERT INTO mac_ip_addresses (macAddress, ipAddress) VALUES ('{0}','{1}');".format(mac, ip)
        conn.execute(query)
    conn.commit()
    showDevices()
else:
    showDevices()
    for s,r in ans:
        mac=(r.sprintf("%Ether.src%"))
        ip=(r.sprintf("%ARP.psrc%"))
        query = "SELECT macAddress,ipAddress FROM mac_ip_addresses WHERE macAddress = '{0}';".format(mac)
        result = conn.execute(query)
        row = result.fetchone()
        if(row):
            if(row[1] != ip):
                reply = raw_input(mac + " this address is already in whitelist with {0} IP address.\nWould you like to update IP adress to {1} y/n :".format(row[1],ip))
                if (reply == 'e'):
                    query = "UPDATE mac_ip_addresses SET ipAddress = '{0}' WHERE macAddress = '{1}';".format(ip,mac)
                    conn.execute(query)
                    conn.commit()
                    print "Updated: " + mac + " -- " + ip
        else:
            reply = raw_input("A new device has been detected.\nMac Address: {0} IP Address: {1}\nWould you like to add this device to whitelist? y/n :".format(mac,ip))
            if (reply == 'e'):
                query = "INSERT INTO mac_ip_addresses (macAddress, ipAddress) VALUES ('{0}','{1}');".format(mac, ip)
                conn.execute(query)
                conn.commit()


conn.close()
