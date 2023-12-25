import random

chars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*()?'
password = ''

print("Welcome to Bryce's Password Gen")
print("")
print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\ ")
print("")

length = input("Password Length: ")
len = int(length)

print("Generating password of length", len, "......")

for x in range(len):
	password += random.choice(chars)

print(password)
