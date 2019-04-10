import pil
import stegano

from stegano import lsb


def decode():
	img = input(" Enter the file name w/ extensions")
	message = lsb.reveal(img)
	return message
def encode():
	img = input(" Enter the file name w/ extensions")
	message = input("Enter the message you want to hide")
	secret = lsb.hide (img, message)
	new_name = "hidden_" + img
	secret.save(new_name)
def main(): 
	
		a = int(input("::  ::\n"
	
			"1. Encode\n 2. Decode\n")) 
	
		if (a == 1): 
		
			encode() 
	
	
	elif (a == 2): 
		
			print("Decoded word- " + decode()) 
	
		else: 
		
			raise Exception("Enter correct input") 

if __name__ == '__main__' :
	main()