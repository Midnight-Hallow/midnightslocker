# pseudo code  destinty   rewards for quest ,  checkpoints,   if you die you only go back to the most recent check point

counter = 0;

string = "Joe"
# this is a string


# computers start at level zero

# this is a list, simple list, one dimension
# This is the Chapters List. These are the levels avialable to play on. Remember, this is just a basic game.
chapters = [ "start", "ship stranded on ice planet","asteroid chase", "swamp teacher green jedi master","death and more death", "you wish you were dead", "no really, give up now" ]


# https://stackoverflow.com/questions/6667201/how-to-define-a-two-dimensional-array-in-python?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa

# Creates a list containing 5 lists, each of 2 items, all set to 0

#  1a,1b
#  2a,2b
#  3a,3b
#  4a,4b
#  5a,5b
#  6a,6b
# as many levels as we want

# today is June 7th  we added code for choice A or B

# on may 27th we added functions called and and ask level



# https://snakify.org/lessons/two_dimensional_lists_arrays/


matrix = [["a) Stowaway on Ship","b) Go back home"],["a) Attempt to land the falling ship","b) Brace for impact"]] 

matrix2 = [["a) Burn the extra supplies to stay warm","b) Eat alien corpse"],["a) Build shelter out of parts from the crashed ship","b) Explore supposedly abandoned cave"]] 

matrix3 = [["a) Leave asteroid field as soon as possible","b) Dodge and shoot asteroids"],["a) Call for reinforcement","b) Pursue enemy ship and try to capture them"]]

matrix4 = [["a) Follow green master","b) Attack green master"],["a) Find ancient sword","b) Refuse a probably epic quest"]]

matrix5 = [["a) Stay and find help for your friend","b) Pursue the Stranger"],["a) Find and defeat Stranger","b) Fall back to base"]]

matrix6 = [["a) Attack enemy soilders","b) Give up"],["a) Rally your allies and fight the Blight Army","b) Surrender to the Blight Army"]]

# function defined with def , it has no parameters, no return value
def  start():
    print("game has started", " you are on level ",  counter )
    print("here is what you find: ",  chapters[counter])

# This is the askLevel function. This function helps the player choose the level they want to play on, with it's few questions and outcomes.
def askLevel(counter):
    humanLevelAnswer = int(input("what level do you want"))
    counter = humanLevelAnswer
    print("let's try that level.... please wait .... ");
    print("here is what you find: ",  chapters[counter])
    survivalQuestion(counter) 
    return counter
    # return the value at the end of the fuction

# This is the survivalQuestion function. This is tha function that creates the level's basic challenge life/death questions. They consist of choice A or B. Pick the right one!
def survivalQuestion(counter):
    # think of some fun if statments
    print(matrix2[0][0])
    print(" ")
    print(matrix2[0][1])
    print(" ")
    # before the function ends, make it return a value

    humananswerAB = input("press a or b please ")


    return counter




start()
counter = askLevel(counter)
print(" ")

# comment out this code below
# counter = nextLevel(counter)
# comment out the code above,  bad broke all my code


print("end of game, counter value: ", counter)



