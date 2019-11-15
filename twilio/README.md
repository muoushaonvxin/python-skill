
```shell
[root@zhangyz ~]# /usr/local/python34/bin/pip install twilio
DEPRECATION: Python 3.4 support has been deprecated. pip 19.1 will be the last one supporting it. Please upgrade your Python as Python 3.4 won't be maintained after March 2019 (cf PEP 429).
Collecting twilio
  Downloading https://files.pythonhosted.org/packages/17/3c/86d481c25a5ad865e374952bd608159066cca222468e0eeb8abf93760a8a/twilio-6.33.1.tar.gz (396kB)
     |████████████████████████████████| 399kB 102kB/s 
Requirement already satisfied: six in /usr/local/python34/lib/python3.4/site-packages (from twilio) (1.11.0)
Collecting pytz (from twilio)
  Downloading https://files.pythonhosted.org/packages/e7/f9/f0b53f88060247251bf481fa6ea62cd0d25bf1b11a87888e53ce5b7c8ad2/pytz-2019.3-py2.py3-none-any.whl (509kB)
     |████████████████████████████████| 512kB 72kB/s 
Collecting PyJWT>=1.4.2 (from twilio)
  Downloading https://files.pythonhosted.org/packages/87/8b/6a9f14b5f781697e51259d81657e6048fd31a113229cf346880bb7545565/PyJWT-1.7.1-py2.py3-none-any.whl
Requirement already satisfied: requests>=2.0.0 in /usr/local/python34/lib/python3.4/site-packages (from twilio) (2.18.4)
Requirement already satisfied: certifi>=2017.4.17 in /usr/local/python34/lib/python3.4/site-packages (from requests>=2.0.0->twilio) (2017.7.27.1)
Requirement already satisfied: urllib3<1.23,>=1.21.1 in /usr/local/python34/lib/python3.4/site-packages (from requests>=2.0.0->twilio) (1.22)
Requirement already satisfied: chardet<3.1.0,>=3.0.2 in /usr/local/python34/lib/python3.4/site-packages (from requests>=2.0.0->twilio) (3.0.4)
Requirement already satisfied: idna<2.7,>=2.5 in /usr/local/python34/lib/python3.4/site-packages (from requests>=2.0.0->twilio) (2.6)
Installing collected packages: pytz, PyJWT, twilio
  Running setup.py install for twilio ... done
Successfully installed PyJWT-1.7.1 pytz-2019.3 twilio-6.33.1
```
