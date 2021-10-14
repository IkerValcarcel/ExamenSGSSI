#!/bin/bash
DIA=$(date +"%d-%m-%Y")
AYER=$(date -d yesterday +%Y-%m-%d)
if [ -z "$(ls -A /home/iker/Backup_Seguridad/)" ]; then
	mkdir /home/iker/Backup_Seguridad/$DIA
	rsync -av /home/iker/Desktop/Seguridad /home/iker/Backup_Seguridad/$DIA
else
	mkdir /home/iker/Backup_Seguridad/$DIA
	rsync -av --compare-dest=/home/iker/Backup_Seguridad/$AYER /home/iker/Desktop/Seguridad /home/iker/Backup_Seguridad/$DIA
fi
mkdir /home/iker/Backup_SGSSI/$DIA
sudo mysqldump -u root -p SGSSI > /home/iker/Backup_SGSSI/$DIA/$DIA.sql
