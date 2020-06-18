import random
list1 = ["0","1","2","3","4","5","6","7","8","9"]
num = random.sample(list1, 4)
ans = "".join(num)
Guess = input("Enter 4 different numbers: ")

while int(Guess) in range(0, 10000):
    A = 0
    B = 0
    if Guess == ans:
        print("Bingo! The answer is ", ans)
        break
    else:
        if Guess[0] in num and Guess[0] == ans[0]:
            A += 1
        elif Guess[0] in num and Guess[0] != ans[0]:
            B += 1

        if Guess[1] in num and Guess[1] == ans[1]:
            A += 1
        elif Guess[1] in num and Guess[1] != ans[1]:
            B += 1

        if Guess[2] in num and Guess[2] == ans[2]:
            A += 1
        elif Guess[2] in num and Guess[2] != ans[2]:
            B += 1      

        if Guess[3] in num and Guess[3] == ans[3]:
            A += 1
        elif Guess[3] in num and Guess[3] != ans[3]:
            B += 1  

        print (A ,"A", B, "B")
        Guess = input("Enter again: ")



