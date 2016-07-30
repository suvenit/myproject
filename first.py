#!/usr/bin/env python
statement=raw_input("Please Describe yourself:")
mylist=[]
for item in statement:
	mylist.append(item)
print mylist
ilist=list(set(mylist))
ilist.sort()
print ilist
for item in ilist:
   count=mylist.count(item)
   print "The number of occurrences of item %s in my statement is %d" %(item,count)
