#print sum of digits of a number
def sum_of_digit(num):
    sum=0
    while num>0:
        rem=num%10
        sum+=rem
        num//=10

    return sum
print(sum_of_digit(123))


#printining the longest word in a sentence
def longest_word(sentence):
    maxw=""
    for i in sentence.split():
        if len(i)>len(maxw):
            maxw=i
        print(maxw)
longest_word("find the longest word")