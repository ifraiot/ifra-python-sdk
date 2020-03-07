from setuptools import setup
setup(
  name = 'ifra-sdk',
  packages = ['ifra-sdk'],  
  version = '1.0.0',
  description = 'Client library of Python, connect to IFRA IIoT Platform.',
  author = 'IFRA IIoT',
  author_email = 'support@ifrasoft.com',
  url = 'https://github.com/ifraiot/ifra-python-sdk', 
  keywords = ['ifra','iot','mqtt'],  
  classifiers = [],
  install_requires=['paho-mqtt==1.2.3','requests','certifi'],
)