import random as r
import turtle as t

###############################################################################

# INSTRUCTIONS 

# display rules of game, and set of instructions ########## DONE
# display options for various thing player can do 
# use one loop ############ DONE
# use one if-elif ########## DONE
# 3 functions with docstrings ########## DONE
# one try-except ################ DONE
# one file input/output ############# DONE
# use turtle graphics ########## DONE
# one thing beyond the lectures  - import random ########## DONE

###############################################################################

mainframe = t.Screen()
mainframe.setup(500,500)
mainframe.bgcolor('black')
mainframe.setworldcoordinates(-3, -3, 3, 5)
mainframe.tracer(0)
t.hideturtle() # we dont want it to draw - should be instant board
#t = turtle
empty = []

# coordfile = open("TTTcoordinates.txt", "r+")

# need to create both the X and O pieces, O for the player and X for the computer 
# the circle will be draw according to where the x and y coordinates are when clicked 

def circlepiece(x,y):
    '''
    Draws the circle piece 
    Will be Dark Blue 
    Takes the x and y coordinate which is establsihed by where the player clicks
    And places the blue circle there
    For some reason the y coordinate has to be subtracted by 0.7 for the circle to appear proper
    '''
    t.color('dark blue')
    t.up()
    t.goto(x,y-0.7)
    t.down()
    r = 0.7
    s = 36000
    # r is the radius 
    # s is the steps or the completion of the circle
    t.circle(r, s)
    t.up()
    
def xpiece(x,y):
    '''
    This function draws the x piece 
    This is the computer piece and is not set by the player
    '''
    t.up()
    #t.down() # will make the line come from the middle (CANNOT HAVE)
    length = 10
    t.color('dark red')
    t.goto(x-0.7,y-0.7)
    t.up()
    t.down()
    t.goto(x+0.7,y+0.7)
    t.up()
    #t.down()
    t.goto(x-0.7,y+0.7)
    t.up()
    t.down()
    t.goto(x+0.7,y-0.7)
    t.up()
    
        
# We need to create the rules display
def rules():
    '''
    This is the rules of the game which is written
    '''
    message = 'The following displays tic-tac-toe and the rules are very simple'
    t.up()
    t.goto(-3,4.5)
    t.pencolor('green')
    t.write(message,move=False, font=('arial',10,'bold'))
    message = 'You will play the computer in a game of tic-tac-toe, and you will go first'
    t.up()
    t.goto(-3,4.3)
    t.pencolor('green')
    t.write(message,move=False, font=('arial',10,'bold'))
    message = 'RULES: Click on the area where you would like to place your character'
    t.up()
    t.goto(-3,4.1)
    t.pencolor('pink')
    t.write(message,move=False, font=('arial',10,'bold'))
    message = 'You will be a blue circle'
    t.up()
    t.goto(-3,3.9)
    t.pencolor('pink')
    t.write(message,move=False, font=('arial',10,'bold'))
    message = 'Once you click, the computer will respond by placing a red X'
    t.up()
    t.goto(-3,3.7)
    t.pencolor('pink')
    t.write(message,move=False, font=('arial',10,'bold'))
    message = 'Try and get 3 in a row without the computer getting 3 in a row to win'
    t.up()
    t.goto(-3,3.5)
    t.pencolor('pink')
    t.write(message,move=False, font=('arial',10,'bold'))
    
# we need to create the grid portion of the board

def grid():
    '''
    This is the actual grid portion of the game
    '''
    t.pencolor('dark grey')
    t.pensize(10)
    t.up()
    t.goto(-1,-3)
    t.seth(90)
    t.down()
    t.fd(6)
    t.up()
    t.goto(1,-3)
    t.seth(90)
    t.down()
    t.fd(6)
    t.up()
    t.up()
    t.goto(-3,-1)
    t.seth(0)
    t.down()
    t.fd(6)
    t.up()
    t.goto(-3,1)
    t.seth(0)
    t.down()
    t.fd(6)
    t.up()

def actualboard():
    """
    Will create the tic tac toe board which we will use 
    """
    # The rules in text
    rules()
    # The actual board
    grid()

# For the Circle Piece and X piece, use the x values of (-2,0,2) and y values of (-2,0,2)

values = [-2,0,2]

win1 = [[-2,2],[-2,0],[-2,-2]]
win2 = [[0,2],[0,0],[0,-2]]
win3 = [[2,2],[2,0],[2,-2]]
win4 = [[-2,2],[0,2],[2,2]]
win5 = [[-2,0],[0,0],[2,0]]
win6 = [[-2,-2],[0,-2],[2,-2]]
win7 = [[-2,2],[0,0],[2,-2]]
win8 = [[-2,-2],[0,0],[2,2]]

totalwin = []

totalwin.append(win1)
totalwin.append(win2)
totalwin.append(win3)
totalwin.append(win4)
totalwin.append(win5)
totalwin.append(win6)
totalwin.append(win7)
totalwin.append(win8)

# for j in range((len(totalwin))):
#     print(totalwin[j])

usercoord = []
compcoord = []

def smart_comp_move():
    """
    Implement a smarter computer move by analyzing the current state of the board
    and making strategic decisions to block the player or aim for a win.
    """
    open_spots = [(x, y) for x in values for y in values if (x, y) not in empty]
    
    # Check for potential wins or blocks
    for spot in open_spots:
        test_compcoord = compcoord + [spot]
        for win_combo in totalwin:
            count = sum(1 for coord in test_compcoord if coord in win_combo)
            if count == 2:
                for coord in win_combo:
                    if coord not in test_compcoord:
                        return coord
    
    # If no immediate win/block move, choose a random open spot
    return r.choice(open_spots)

def choose_first_move():
    """
    Prompt the user to choose who goes first: player or computer.
    """
    first_move = mainframe.textinput("Choose First Move", "Who goes first? (player/computer)").lower()
    return first_move

def draw(x,y):
    # takes user input (x,y) from the onclicksreen in the play fucntion BELOW
    # The empty list will add specific coordinates from where previous circle and x's have been placed,
    # This can be used to ensure circles and x's do not overlap
    les1 = [-2]
    try:
        x = float(x)
        y = float(y)
        # Makes sure there is actual input 
        # Make sures the onscreen click works because it is a new function
    except:
        t.onscreenclick()
    if x > -1 and x < 1 :
        x = 0
    elif x < -1 and x > -3:
        x = -2
    elif x > 1 and x < 3:
        x = 2
    if y > -1 and y < 1:
        y = 0
    elif y >-3 and y < -1:
        y = -2 
    elif y > 1 and y < 3:
        y = 2
    for i in range(3):
        if i % 2 == 0 :
            les1.append(i)
    #for i in range(5):
    values = [x, y]
    # THIS IS FOR THE CIRCLE TO DRAW
    if x in les1 and y in les1 and (values not in empty):
        # string = '(' + str(x) + ', ' + str(y) + ')'
        # coordfile = open("TTTcoordinates.txt", "r+")
        # coordfile.write(string) 
        # print(string)
        #coordinates += [x,y]
        circlepiece(x,y)
        empty.append(values)
        usercoord.append(values)
    xx, xy = smart_comp_move()
    newvalues = [xx, xy]
    # THIS IS FOR THE X TO DRAW
    if (xx != x or xy != y) and (newvalues not in empty):
        xpiece(xx,xy)
        empty.append(newvalues)
        compcoord.append(newvalues)
    else :
        yval = [-2, 0, 2]
        xval = [-2, 0, 2]
        yval.remove(xy)
        xval.remove(xx)
        xx, xy = smart_comp_move()
        newvalues = [xx, xy]
        if (xx != x or xy != y) and (newvalues not in empty) :
            xpiece(xx,xy)
            empty.append(newvalues)
            compcoord.append(newvalues)
        else :
            yval = [-2, 0, 2]
            xval = [-2, 0, 2]
            yval.remove(xy)
            xval.remove(xx)
            xx, xy = smart_comp_move()
            newvalues = [xx, xy]
            if (xx != x or xy != y) and (newvalues not in empty):
                xpiece(xx,xy)
                empty.append(newvalues)
                compcoord.append(newvalues)
            else :
                yval = [-2, 0, 2]
                xval = [-2, 0, 2]
                yval.remove(xy)
                xval.remove(xx)
                xx, xy = smart_comp_move()
                newvalues = [xx, xy]
                if (xx != x or xy != y) and (newvalues not in empty):
                    xpiece(xx,xy)
                    empty.append(newvalues)
                    compcoord.append(newvalues)
                else :
                    yval = [-2, 0, 2]
                    xval = [-2, 0, 2]
                    yval.remove(xy)
                    xval.remove(xx)
                    xx, xy = smart_comp_move()
                    newvalues = [xx, xy]
                    if (xx != x or xy != y) and (newvalues not in empty):
                        xpiece(xx,xy)
                        empty.append(newvalues)
                        compcoord.append(newvalues)
                    else :
                        yval = [-2, 0, 2]
                        xval = [-2, 0, 2]
                        yval.remove(xy)
                        xval.remove(xx)
                        xx, xy = smart_comp_move()
                        newvalues = [xx, xy]
                        if (xx != x or xy != y) and (newvalues not in empty):
                            xpiece(xx,xy)
                            empty.append(newvalues)
                            compcoord.append(newvalues)
    # if len(compcoord) >= 3:
    #     return compcoord
    # if len(usercoord) >= 3:
    #     return usercoord
    #     print(usercoord)
    # if len(empty) > 8 :
    #     return empty
    win(compcoord, usercoord, empty)
    
def win(compcoord, usercoord, empty):
    if len(usercoord) >= 3:
        for i in totalwin:
                newuser = []                
                for j in usercoord :
                    if j in i:
                        newuser.append(j)
                        if len(newuser) == 3:
                            j = 3
                            mainframe.textinput("Game over!","You WON!")
                            with open('winningcoordinates.txt', 'a+') as myfile:
                                string = 'The winning coordinates for this game are by the user are' + str(newuser) +'\n'
                                myfile.write(string)
                                break
                                
    if len(compcoord) >= 3:
        for i in totalwin:
                newcomp = []
                for x in compcoord :
                    if x in i:
                        newcomp.append(x)
                        if len(newcomp) == 3:
                            #print(True)
                            mainframe.textinput("Game over!","You LOST!")
                            with open('winningcoordinates.txt', 'a+') as myfile:
                                    string = 'The winning coordinates for this game by the computer are' + str(newcomp) + '\n'
                                    myfile.write(string)
                                    break
    if len(empty) == 9:
        mainframe.textinput("Game over!","TIE!")
        with open('winningcoordinates.txt', 'a+') as myfile:
                string = 'The game ended in a tie'
                myfile.write(string)
                
         
def play():
    actualboard()
    
    first_move = choose_first_move()
    
    if first_move == "player":
        t.onscreenclick(draw)
    elif first_move == "computer":
        xx, xy = r.choice(values), r.choice(values)
        xpiece(xx, xy)
        empty.append([xx, xy])
        compcoord.append([xx, xy])
        t.onscreenclick(draw)
    
play()
t.mainloop()
t.done()
