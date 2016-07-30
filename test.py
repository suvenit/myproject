#!/usr/bin/env python
SampleList=[]
while True:
	city=raw_input("please enter your city: ")
	if city=='finish':
		break
	else:
		SampleList.append(city)
		
SampleList=SampleList.sort()
print SampleList
