def main():

	
	w= open("index.html", "a+")
	
	name = input("What is your name?")

	w.write(name)	

	prop = input("Given all the information you've learned, what system might you propose?")
	
	w.write(prop)
	
	w.close()

if __name__== "__main__":
	
	main()
	
