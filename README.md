# Kripton Guard
Receive notification when a new device is connected to the network
## Introduction
Kripton Guard, saves MAC addresses to an SQLite database by sending ARP packets to your network in the learning process, when the learning process is completed, it compares the devices in the network to the devices already registered in the database and sends a notification to your phone if a new device is found.

Kripton Guard uses [Google Firebase Authentication](https://firebase.google.com/docs/auth/) for authentication, associates your  `user id` with `device id` and saves it in [Google Realtime Database](https://firebase.google.com/docs/database/).  It sends you notifications via [Google Firebase Cloud Messaging](https://firebase.google.com/docs/cloud-messaging/) when new device is found.

## Prerequisites
Kripton Guard uses [scapy](https://github.com/secdev/scapy), [pyrebase](https://github.com/thisbejim/Pyrebase), [pyfcm](https://github.com/olucurious/PyFCM), [python-crontab](https://github.com/doctormo/python-crontab) libraries and you can easily installed them with pip:
```
pip install -r requirements.txt
```
## Installation
### Android
You need to install kripton-guard.apk to your Android Phone. After that fill in the required information on the form and create an account.
### Python
*Clone the repository:
```
git clone https://github.com/COMU/kripton-guard.git
```
Edit `[SETTINGS]` section in [Python/kripton-guard.conf](https://github.com/COMU/kripton-guard/blob/master/Python/kripton-guard.conf "kripton-guard.conf").
*&nbsp;&nbsp;&nbsp;&nbsp;Note: `repeattime` gets value in minutes*

Run [Python/install.py](https://github.com/COMU/kripton-guard/blob/master/Python/install.py "install.py") with `sudo` privileges:
```
sudo python install.py
```
If Kripton Guard is installed correctly, [kripton-guard.conf](https://github.com/COMU/kripton-guard/blob/master/Python/kripton-guard.conf "kripton-guard.conf") file will be moved to `/etc/kripton-guard` and [kripton-guard.py](https://github.com/COMU/kripton-guard/blob/master/Python/kripton-guard.py "kripton-guard.py") file to `/opt/kripton-guard`.

After a few minutes, your phone will be notified when a new device joins to your network.

## License

This project is licensed under the **GNU General Public License v3.0** - see the [LICENSE.md](https://github.com/COMU/kripton-guard/blob/master/LICENSE) file for details
