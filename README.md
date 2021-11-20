# Riddle-Poll-BOT
This is a script in python that automate vote process in Riddle.com

Setup and customize Tor Config

Tor libs are te path /var/lib/tor so lets copy that folder in multiple time
root# cp –r /var/lib/tor /var/lib/tor1
root# cp –r /var/lib/tor /var/lib/tor2
root# cp –r /var/lib/tor /var/lib/tor3
root# cp –r /var/lib/tor /var/lib/tor4
root# cp –r /var/lib/tor /var/lib/tor5
root# cp –r /var/lib/tor /var/lib/tor6
root# cp –r /var/lib/tor /var/lib/tor7
root# cp –r /var/lib/tor /var/lib/tor8
root# cp –r /var/lib/tor /var/lib/tor9

Tor configurations are located at /etc/tor/torrc and lets write configuration 
Firstly generate tor hash password use command:
tor --hash-password landaprojekt 

File 1
root# nano /etc/tor/torrc1  paste following code
SocksPort 9050
ControlPort 9051
HashedControlPassword 16: hashi I password te tor
DataDirectory /var/lib/tor1

File 2
root# nano /etc/tor/torrc2  paste following code
SocksPort 9060
ControlPort 9061
HashedControlPassword 16: hashi I password te tor
DataDirectory /var/lib/tor2

File 3
root# nano /etc/tor/torrc3  paste following code
SocksPort 9070
ControlPort 9071
HashedControlPassword 16: hashi I password te tor
DataDirectory /var/lib/tor3

File 4
root# nano /etc/tor/torrc4  paste following code
SocksPort 9080
ControlPort 9081
HashedControlPassword 16: hashi I password te tor
DataDirectory /var/lib/tor4

File 5
root# nano /etc/tor/torrc5  paste following code
SocksPort 9090
ControlPort 9091
HashedControlPassword 16: hashi I password te tor
DataDirectory /var/lib/tor5

File 6
root# nano /etc/tor/torrc6  paste following code
SocksPort 9100
ControlPort 9101
HashedControlPassword 16: hashi I password te tor
DataDirectory /var/lib/tor6

File 7
root# nano /etc/tor/torrc7  paste following code
SocksPort 9200
ControlPort 9201
HashedControlPassword 16: hashi I password te tor
DataDirectory /var/lib/tor7

File 8
root# nano /etc/tor/torrc8  paste following code
SocksPort 9300
ControlPort 9301
HashedControlPassword 16: hashi I password te tor
DataDirectory /var/lib/tor8

File 9
root# nano /etc/tor/torrc9  paste following code
SocksPort 9400
ControlPort 9401
HashedControlPassword 16: hashi I password te tor
DataDirectory /var/lib/tor9

Action start
Firstly we start Tor instances, in total we have in total 9 threads thas use different port and use different IP and always will have different address

root# tor –f /var/lib/tor1 & tor –f /var/lib/tor2 & tor –f /var/lib/tor3 & tor –f /var/lib/tor4 & tor –f /var/lib/tor5 & tor –f /var/lib/tor6 & tor –f /var/lib/tor7 & tor –f /var/lib/tor8 & tor –f /var/lib/tor9

Now let start script

root# Python3 Script_Name.py




