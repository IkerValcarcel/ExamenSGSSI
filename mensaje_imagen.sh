#!/bin/bash
for f in *
do
	hash=$(md5sum $f)
	echo("$hash[0]")
	if [[ $hash[0] -eq "e5ed313192776744b9b93b1320b5e268" ]]
	then 
		stegosuite -x $f
		break
	fi
	 
done
