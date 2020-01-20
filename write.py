import os
from git import Repo
from git import Actor


def main():


	w= open("index.html", "a+")
	
	name = input("What is your name?\n")
	

	w.write("\n" + name + "\n")
	

	prop = input("Given all the information you've learned, what system might you propose? \n")
	
	w.write(prop + "\n")
	
	w.close()

	repo_path = os.getenv('GIT_REPO_PATH')

	repo = Repo(repo_path)

	assert not repo.bare

	index = repo.index
	
	index.commit(name)

	os.system("git push --all")

if __name__== "__main__":
	
	main()
	
