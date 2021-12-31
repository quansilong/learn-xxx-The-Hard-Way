#!/usr/bin/env bash

for I in `ls`; do 
if [ -d $I ] ; then 
	echo $I;
	cd ${I};
	qvasp -clean;
	ls; echo start calculate;
	vasp_run.sh | tee stdout;
	echo; echo;
	cd ..;
fi; 
done
