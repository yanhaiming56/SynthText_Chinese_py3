#!/bin/sh

> fontlist.txt
for file in more_font/*
do
	
	if test -f ${file}
	then
		echo "${file}"
		echo "${file}" >> fontlist.txt
	fi
done

