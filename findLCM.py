# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 11:27:38 2017

@author: rmaskus
"""

# lowest common multiple

#smallest number evenly divisable by every number 1 to 20
# pick a solution thats small
# check that it's divisible by 20, 19, 18 etc
# if it isn't increase the solution and try again

solution = 20
solved = 0

while not solved:
    for divisor in range (20,1, -1):
        print("trying:", solution)
        print(solution % divisor)
        if solution % divisor == 0:   
            if divisor == 2:
                solved = 1
            else:
                divisor = 20
                solution += 1
        
        

        