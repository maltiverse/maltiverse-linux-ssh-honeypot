![](https://maltiverse.com/assets/images/logo/logo_letters_black.png)

# maltiverse-linux-ssh-honeypot
Maltiverse Linux SSH honeypot is a script to contribute to the Maltiverse Search Engine [maltiverse.com](https://www.maltiverse.com/).

Maltiverse is an open IoC search engine to support the cybersecurity community on their research an investigations. (https://whatis.maltiverse.com/)

There is a REST API to handle the service and help automation which is defined here:

https://app.swaggerhub.com/apis-docs/maltiverse/api/1.0.0-oas3

This script looks for attacking IP's into SSH log files in a Linux system and pushes them to the Maltiverse Search Engine.


## [1 - Requirements](#table-of-contents)

There are sereval requirements for this script to be accomplished:
 * Server running Linux OS
 * Service SSH running and exposed to the internet
 * Outbound connectivity to the resource https://api.maltiverse.com
 * A Maltiverse user account with Team Researcher privileges. Only team researchers are allowed to upload indicators into Maltiverse. Create an account, then create or join a team, and get Team Researcher permissions!

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

  ### A) By settingenvironment variables:
  Parameters "--email" and "--password" running the command from the console will provide credentials to the script
  ```
  export MALTIVERSE_EMAIL=test@maltiverse.com
  export MALTIVERSE_PASSWORD=secret!
  python /opt/maltiverse_linux_ssh_honeypot.py
  ```

 ### B) By entry parameters:
 Parameters "--email" and "--password" running the command from the console will provide credentials to the script
 ```
 python /opt/maltiverse_linux_ssh_honeypot.py --email test@maltiverse.com --passwords secret!
 ```
