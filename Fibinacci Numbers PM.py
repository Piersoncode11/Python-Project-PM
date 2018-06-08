import turtle
myTurtle = turtle.Turtle()
myTurtle.shape("turtle")

prevNum = 0
currNum = 1
nextNum = prevNum + currNum
number_of_terms = 15
myTurtle.color('red')
for i in range(number_of_terms):
    
    print(currNum)
    for f in range(currNum - prevNum):
        myTurtle.right(360/currNum)
        myTurtle.forward(10)

    nextNum = currNum + prevNum
    prevNum = currNum
    currNum = nextNum
