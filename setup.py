from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setup(
  name = 'ifra_sdk',
  packages = ['ifra_sdk'],  
  version = '1.0.5',
  description = 'Client library of Python, connect to IFRA IIoT Platform.',
  author = 'IFRA IIoT',
  author_email = 'support@ifrasoft.com',
  url = 'https://github.com/ifraiot/ifra-python-sdk', 
  keywords = ['ifra','iot','mqtt'],  
  classifiers = [],
  install_requires=['paho-mqtt==1.2.3','requests','kpn-senml==1.0.1'],
)
