"""Size: 7 x 21 
---------.|.---------
------.|..|..|.------
---.|..|..|..|..|.---
-------WELCOME-------
---.|..|..|..|..|.---
------.|..|..|.------
---------.|.---------"""



N = 7
M = 21

i = 1
for x in range(1,N):
    print(('.|.' * i).center(M, '-'))
    if (x < N // 2):
        i = i + 2
    elif (x == N // 2):
        print ("WELCOME".center(M, '-'))       
    else:
        i = i - 2

#for _ in range((N // 2) + 1):
#    i = i + 2
#    print(('.|.' * i).center(M, '-'))

#print ("WELCOME".center(M, '-'))

#for _ in range((N // 2) + 1):
#    i = i - 2
#    if i > 0:
#        print(('.|.' * i).center(M, '-'))