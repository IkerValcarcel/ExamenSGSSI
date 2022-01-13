sudo iptables -A INPUT -p tcp -m tcp --sport 80 -j DROP
sudo iptables -A OUTPUT -p tcp -m tcp --dport 80 -j DROP 
