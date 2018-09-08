#I made this for soccer but this can be used with basketball, hockey, etc. 
#Basically, in a stationary position, I move the ball with each foot in the direction (given by the app) and pull it back to the stationary position. 
#I switch each foot when instructed to by the program.

from random import randint
import time
x = ["^^UP^^", "^^UP^^", "^^UP^^","^^UP^^","<<SIDE>>","<<SIDE>>", "<<SIDE>>","<<SIDE>>","vvDOWNvv","vvDOWNvv","vvDOWNvv","vvDOWNvv","SWITCH SIDES"]
y = 0
z = " "
a = x


#Next challenge: Make it so the probability of switch feet is lower than the rest of the elements
while y < 30:
        y = y + 1
        if y == 1:
                z = x[randint(0,12)]
                print(z)
                time.sleep(.65)
        else:
                for element in x:
                        if element == z:
                                if element =="SWITCH SIDES":
                                        a.remove(element)
                                        z = a[randint(0,11)]
                                        print(z)
                                        a.append(element)
                                        time.sleep(1.2)
                                else:
                                        for number in [0, 1, 2, 3]:
                                                a.remove(element)
                                        z = a[randint(0,8)]
                                        print(z)
                                        for number in [0, 1, 2, 3]:
                                                a.append(element)
                                        time.sleep(.65)
                        
        
        
