import turtle
myTurtle = turtle.Turtle()
myTurtle.shape("turtle")

prevNum = 0
currNum = 1
nextNum = prevNum + currNum
fibNums = [prevNum, currNum]
number_of_terms = 15
myTurtle.color('red')
for i in range(14):
    nextNum = currNum + prevNum
    prevNum = currNum
    currNum = nextNum
    fibNums.append(currNum )

for x in fibNums:
    print(x)
    myTurtle.right(90)
    myTurtle.forward(x / 2)
    
