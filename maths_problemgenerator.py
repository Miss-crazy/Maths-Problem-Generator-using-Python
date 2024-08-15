#MATH PROBLEM GENERATOR
import random 
max_num = 12
min_num = 2
operator_list=["+","-","*"]

def evaluation():
    left=random.randint(min_num , max_num)
    right =random.randint(min_num , max_num)
    symbol = random.choice(operator_list)
    exp = str(left)+symbol+str(right)
    answer = str(eval(exp))
    
    return exp,answer

def play():
    print("ANSWER THESE 10 MATHS PROBLEMS") 
    for i in range(10):
        exp,answer=evaluation()
        print("Problem #",i+1," : ")
        print(exp," = ")
        player_ans =input()
        
        while player_ans!=answer:
             print(exp," = ")
             player_ans = input()
           
    print("WELL DONE!")
play()