#################################### prac1 ###############################33 

# a = int(input('Enter the num : '))
# b = []
# for i in range (0,a):
#     b.append(i)
# print(b)

# c = map(lambda x:x**2,b)
# print(list(c))


#################################### prac2 ###############################33 

# a = 0
# for i in range (1,1001): 
#     if i % 3 == 1 : a += i
# print(a)

#################################### prac3 ###############################33 

import pyttsx3

a = pyttsx3.init()
a.say('hi amir')
a.runAndWait()