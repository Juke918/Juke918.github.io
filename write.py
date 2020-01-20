import os

def main():

	
	w= open("index.html", "a+")
	
	name = input("What is your name?\n")
	

	w.write("\n" + name + "\n")
	

	prop = input("Given all the information you've learned, what system might you propose? \n")
	
	w.write(prop + "\n")
	
	w.close()

	os.system("git push --all")

if __name__== "__main__":
	
	main()
	
