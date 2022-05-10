import json #importing json file
from difflib import get_close_matches

data = json.load(open("data.json")) #json file name to import is located same as this program

def translate(w):
	w = w.lower()
	if w in data:
		return data[w]
	elif len(get_close_matches(w,data.keys())) > 0:
		yesno = input ("Did you mean %s instead? Yes or No: " % get_close_matches(w,data.keys())[0])
		if yesno == "Y" or "y" or "Yes" or "yes":
			return data [get_close_matches(w,data.keys())[0]]
		elif yesno == "N" or "n" or "No" or "no":
			return "The word does not matched. Please double check again"
		else:
			return "We did not understand"
	else :
		return "The word not found"

word = input("Enter your word: ")
output = translate(word) #call the function
if type(output) == list:
	for item in output:
		print(item)
else:
	print(output)
