#!/usr/bin/python3

from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name="kripton-guard",
    version="0.5",
    long_description=readme(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.6',
        'Topic :: System :: Networking :: Monitoring',
      ],
    author="Okan Ozdemir",
    author_email="okn.ozdemir@gmail.com",
    description="Receive notification when a new device is connected to the network.",
    license="GPL-3.0",
    url="https://github.com/COMU/kripton-guard",

    install_requires=['scapy','pyrebase','pyfcm','python-crontab','configparser'],
    packages=['kripton-guard'],
    scripts=['kripton-guard/kripton-guard'],
    data_files=[('/etc/kripton-guard', ['kripton-guard/kripton-guard.conf'])],
    include_package_data=True,
    zip_safe=False
)
