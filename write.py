import os
from git.test.lib import TestBase
from git.test.lib.helper import with_rw_directory
import os.path

class Add(TestBase):
	
	def tearDown(self):
	    import gc
	    gc.collect()


	@with_rw_directory

	def main(self, rw_dir):

		from git import Repo

		w= open("index.html", "a+")
		
		name = input("What is your name?\n")
		

		w.write("\n" + name + "\n")
		

		prop = input("Given all the information you've learned, what system might you propose? \n")
		
		w.write(prop + "\n")
		
		w.close()

		#repo_path = os.getenv('GIT_REPO_PATH')

		repo = Repo(self.Users/julianpk/Desktop/coding/euthanasia_game/Juke918.github.io)

		assert not repo.bare

		index = repo.index

		assert len(list(index.iter_blobs())) == len([o for o in repo.head.commit.tree.traverse() if o.type == 'blob'])

		for (_path, _stage), entry in index.entries.items():

			pass
		
		self.assertEqual(index.commit("name").type, 'commit')

		os.system("git push --all")
       


if __name__ == "__main__":
    objName = Add()
    objName.main() 


	
