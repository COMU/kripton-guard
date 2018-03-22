# Kripton Guard
Receive notification when a new device is connected to the network.
## Introduction
Kripton Guard, saves MAC addresses to a SQLite database by sending ARP packets to your network in the learning process, when the learning process is completed, it compares the devices in the network with the devices that already registered in the database. If the device is unknown it sends a notification to your phone.

Kripton Guard uses [Google Firebase Authentication](https://firebase.google.com/docs/auth/) for authentication, associates your  `user id` with `device id` and saves it in [Google Realtime Database](https://firebase.google.com/docs/database/).  It sends you notifications via [Google Firebase Cloud Messaging](https://firebase.google.com/docs/cloud-messaging/) when new device is found.

## Prerequisites

Kripton Guard uses [scapy](https://github.com/secdev/scapy), [pyrebase](https://github.com/thisbejim/Pyrebase), [pyfcm](https://github.com/olucurious/PyFCM), [python-crontab](https://github.com/doctormo/python-crontab) and these libraries will be installed automatically when installing kripton-guard pip package but you can also install them with the command below:
```
pip install -r requirements.txt
```
## Installation

### Android
Google Play Link: [Kripton-Guard](https://play.google.com/store/apps/details?id=com.comu.oozdemir.kriptonguard "Kripton-Guard")

### Python

![](https://media.giphy.com/media/2kP6H6uOH2UXGdykiE/giphy.gif)

```
pip install kripton-guard
```

Edit `[SETTINGS]` section in [/etc/kripton-guard/kripton-guard.conf](https://github.com/COMU/kripton-guard/blob/master/kripton-guard/kripton-guard.conf "kripton-guard.conf").

Run the program with:

```
sudo kripton-guard
```

After a few minutes, your phone will start to get notification whenever a new device join to your network.

## License

This project is licensed under the **GNU General Public License v3.0** - see the [LICENSE.md](https://github.com/COMU/kripton-guard/blob/master/LICENSE) file for details.
