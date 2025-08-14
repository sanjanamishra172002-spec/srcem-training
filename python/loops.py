#print numbers between 1 to 100 that are divisble by 3 and 5

for num in range(1,16):
    if (num%3==0) or (num%5==0):
        print(num)



#print a star diamond pattern
for i in range(1,6,2):
    space=(4-i)//2
    print(" "*space+ "*"*i)


#count consonents in a string
sentence="hello world"
vowels="aeiouAEIOU"
count=0
for i in sentence:
    if i not in vowels:
        count += 1
print("number of consonants:",count)


#number guessing game
secret_number=8
num = int(input("guess the number"))
if num==secret_number:
    print("correct! you guessed it ")
else:
    print("wrong, try again")
