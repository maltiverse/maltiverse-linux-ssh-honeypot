![](https://maltiverse.com/assets/images/logo/logo_letters_black.png)

# maltiverse-linux-ssh-honeypot
Linux SSH honeypot to contribute to the Maltiverse Search Engine [maltiverse.com](https://www.maltiverse.com/).

Maltiverse is an open IoC search engine to support the cybersecurity community on their research.

There is a REST API to handle the service and help automation which is defined here:

https://app.swaggerhub.com/apis-docs/maltiverse/api/1.0.0-oas3

This script gets attacking IP's from a SSH log in a Linux system and pushes them to the Maltiverse Search Engine.


## [1 - Requirements](#table-of-contents)

There are sereval requirements for this script to be accomplished:
 * Server running Linux OS
 * Service SSH running and exposed to the internet
 * Outbound connectivity to the resource https://api.maltiverse.com

## [2 - Installation](#table-of-contents)

First of all it is required to install python-maltiverse package:
```
pip install git+https://github.com/maltiverse/python-maltiverse
```

Then download the script locally:
```
cd /opt && git clone https://github.com/maltiverse/maltiverse-linux-ssh-honeypot
```
Now the script is located in /opt/maltiverse-linux-ssh-honeypot and ready to be executed


## [3 - Configuration](#table-of-contents)

To execute this script it is required to provide maltiverse username and password to log in and upload the indicators of compromise found.

It can be done in two ways:

 ### By entry parameters:
 ```
 python /opt/maltiverse_linux_ssh_honeypot.py -e test@maltiverse.com -p secret!
 ```
