n1 = input("Number 1 ")
n2 = input("Number 2 ")
import random
result = random.randint(int(f"{n1}") , int(f"{n2}"))
print("The Number 1 is " + str(result))
n3 = input("Number 3 ")
n4 = input("Number 4 ")
result2 = random.randint(int(f"{n3}") , int(f"{n4}"))
print("The Number 2 is " + str(result2))
result3 = result**result2 # math.pow(int(f"{result}") , int(f"{result2}"))
n5 = input("Number 5 ")
n6 = input("Number 6 ")
result4 = int(n5) ** int(n6)
result5 = int(result4) / result2
result6 = int(result3) / result
result7 = result3 / result5
result8 = result6 / result4
result9 = result5 / result3
result10 = result4 / result6
results = [result , result2 , result3 , result4 , int(result5) , int(result6) , result7 , result8 , int(result9) , int(result10)]
for line in results : 
    print(line)
# print(math.fmod(20, 3))  
# print(math.fabs(-66.43))
import math
import random
re1 = random.random()
if re1 >= 0.5 : 
    print("Itis " + str(re1))
else :
    print("Itis not " + str(re1))
re2 = random.normalvariate()
if re2 >= 0 : 
    print("Itis " + str(re2))
else : 
    print("Itis not " + str(re2))
# print(math.ceil(1.4))
print(math.fmod(20, 3))
print(math.fabs(-66.43))
