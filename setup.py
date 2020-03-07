from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setup(
  name = 'ifra-sdk',
  packages = ['ifra-sdk'],  
  version = '1.0.1',
  description = 'Client library of Python, connect to IFRA IIoT Platform.',
  author = 'IFRA IIoT',
  author_email = 'support@ifrasoft.com',
  url = 'https://github.com/ifraiot/ifra-python-sdk', 
  keywords = ['ifra','iot','mqtt'],  
  classifiers = [],
  install_requires=['paho-mqtt==1.2.3','requests','certifi'],
)