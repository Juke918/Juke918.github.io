import os
import git


repo = git.Repo('/Users/julianpk/Desktop/coding/euthanasia_game/Juke918.github.io')

	
def main():

	print("Hello there! Are you ready to play the educational text-based adventure game on euthanasia? (press enter to continue)")


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
	main()
	#write()


	
