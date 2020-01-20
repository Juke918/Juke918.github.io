import os
import git


repo = git.Repo('/Users/julianpk/Desktop/coding/euthanasia_game/Juke918.github.io')

	

def write():

	w= open("index.html", "a+")
	
	name = input("What is your name?\n")
	

	w.write("\n" + "<br>" + name + "\n" + "<br>")
	

	prop = input("Given all the information you've learned, what system might you propose? \n")
	
	w.write(prop + "\n" + "<br>")
	
	w.close()

	os.system("git commit -a --allow-empty-message -m ''")

	os.system("git push --all")	
       


if __name__ == "__main__":
	write()


	
