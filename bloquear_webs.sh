webs=('twitter.com' 'facebook.com' 'youtube.com')
for i in "${webs[@]}"
do
	echo "$i"
	sudo iptables -A OUTPUT -m string --string "$i" --algo kmp --to 65535 -j DROP
done
