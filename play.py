import os
import git
import time


repo = git.Repo('/Users/julianpk/Desktop/coding/euthanasia_game/Juke918.github.io')

	
def main():

	c()

	input("Hello there! Welcome to the best educational text-based adventure game-experience on euthanasia known to humankind! (press enter to continue)")

	c()

	input("Each time you are done reading the given text you can press enter to see the next one")

	c()

	input("Are you ready to begin?")

	c()

	input("You are the Governor of Massachusetts. On the most recent ballot, the people of Massachusetts voted to legalize PAS. It is now your responsibility to craft a system that is \neconomically fair and equitable to all of your constituents.")

	c()

	input("At governer school, you learned that it's important to look at other systems before crafting your own. So you order your minions to research how other states have handled the \nissue of economic disenfranchisement through PAS.")

	c()

	input("You are busy governor, so you ask them to filter down their hours and hours of tedidous reseach into only the most valuable and useful information to making you decision.")

	c()

	input("They come back with two states: California and Oregon.")

	c()

	input("First you look at California")

	c()

	cal = open("cal.txt", "r")

	print(cal.read())

	input("\n")

	c()

	input("Hmm... seems like its very important to regulate to lethal injection manufacturers and companies.")

	c()

	input("Good thing you can alwaus count on AG Healy to lay down THE LAW!") 

	c()
		
	input("Next you look at Oregon")

	c()

	ore= open("ore.txt", "r")

	print(ore.read())

	input("\n")

	c()

	input("Well it doesn't seem like there's a state that has it quite figured out.")

	c()

	input("Your heart sinks as it sets in that you won't be able to copy your proposal from another state...")

	c()

	input('...but all of the sudden, you have a light-bulb moment!')

	c()

	input("You are reminded of governer school's infamous mantra: NEVER GIVE UP.")

	c()

	input("If you can't copy another state, then maybe...")

	c()

	input("..you could copy another country!")

	c()

	input("Immediately, you call up you trusty minions and order them to research other countires with the same stipulations as before.")

	c()

	input("They come back with two countries: Great Britain and Canada")

	c()

	input("First you look at Great Britain")

	c()

	gbr = open("gbr.txt", "r")

	print(gbr.read())

	input("\n")

	c()

	input("It's definitely important that you make sure the programs are dynamic and accessible.") 

	c()

	input("You move on to Canada")

	c()

	can = open("can.txt", "r")

	print(can.read())

	input("\n")

	c()

	input("Although Canada's isn't the perfect model, it does give you hope: You--ahem--the people of Massachusetts could actually make money off of this!")

	c()

	input("And who cares if nobody else has done it? Massachusetts can be the first state to legalize PAS in a economically fair and equitable way!")

	c()

 
	write()


def write():

	w= open("index.html", "a+")
	
	input("It is now time to craft your proposal!")

	c()

	name = input(" At governor school you learned that the most important part of crafting a proposal is writing your name on it, what is your name? \n \n(KEEP IN MIND THAT YOUR RESPONSES WILL BE SAVED AND VIEWABLE BY THE REST OF THE CLASS)\n \n")
	

	w.write("\n" + "<br>" + name + "\n" + "<br>")

	c()
	

	prop = input("Given all the information you've learned, what system do you propose? \n \n")
	
	w.write(prop + "\n" + "<br>")
	
	w.close()

	c()

	os.system("git commit -a --allow-empty-message -m ''")

	os.system("git push --all")	

	time.sleep(2.5028410)

	c()

	input('Great job! You should see your response up on the web page soon.')

	c()

	print('Thanks for playing! \n')


       
def c():

	os.system("clear")

	print("\n")


if __name__ == "__main__":
	main()
	#write()


	

