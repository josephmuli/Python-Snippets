#!/usr/bin/env python2

#here I create variables to show different data types in Python


hello_str = "Hi pal"

hello_int = 21

hello_bool = True

hello_tuple = (21,32)

hello_list = [“Hello,”, “this”, “is”, “a”, “list”]

#I have created an empty list and the following lines use the list type function
#append to add elements to the list
hello_list = list()
hello_list.append("Hello")
hello_list.append("this")
hello_list.append("is")
hello_list.append("a")
hello_list.append("list")


hello_dict = {"first_name" : "Joseph",
	"last_name" : "Muli",
	"eye_color" : "Blue"}


print(hello_list[4])
hello_list[4] += "!"
print(hello_list[4])
