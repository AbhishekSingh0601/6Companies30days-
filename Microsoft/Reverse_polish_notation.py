  #Evaluate Reverse Polish Notation
'''
        You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

        Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
  
'''
#taking input in form of list
tokens=[str(item) for item in input().split(" ")]
#using stack to get first element which is operated
stack=[]

#itterating through tokens
for chip in tokens:

    #if there are no +-*/ operator in the list append in stack as int
    if chip not in "+-/*":
        chip=int(chip)
        stack.append((chip))
    else:
        #taking left and right as last two element of stack
        left,right=int(stack.pop()),int(stack.pop())
        #if chip are operator perform operation with left and right
        if(chip == "+"):
            #appending the operating element as new first element added
            stack.append(right+left)

        elif(chip == "-"):
           stack.append(right-left)


        elif(chip == "*"):
           stack.append(right*left)
        elif(chip=="/"):

            '''
                        for division we should take floor division
                        but in some case like 6 / -132 value is -0.0069 you here truncates to zero 
                        therefore we will keep such case in mind 
            '''
                    
            stack.append(int(right/left))

print(stack[0])
        