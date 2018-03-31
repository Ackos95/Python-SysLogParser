# Python SysLogParser class

Simple python class to parse `syslog` files (both `rfc5424` and `rfc3164` styled)


### Installation and usage

Install package as dependency
```
pipenv install pipenv install git+https://github.com/Ackos95/Python-SysLogParser.git#egg=SysLogParser
```

Usage
```
from SysLogParser.parser import SysLogParser

with open('/var/log/messages.log', 'r') as syslog_file
    lines = syslog_file.readlines()
SysLogParser.parse_rfc5424(lines)
```