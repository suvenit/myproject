#!/usr/bin/env python
Data='i am raajitha i am from hyderabad i am currently in bangalore'
DataSplit=Data.split()
DataSet=list(set(DataSplit))
for element in DataSet:
	print element,DataSplit.count(element)
