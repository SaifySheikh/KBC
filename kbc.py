import random

questions=["q1","q2","q3","q4","q5","q6"]
answers=["a","b","c","d","e","f"]

total=[]
for i in range(len(questions)):
    total.append((questions[i],answers[i]))
  
rounds=3
score=0
updated_questions=questions.copy()
print(updated_questions)
for i in range(rounds):
    question_number=random.randint(0,len(updated_questions)-1)
    question=questions[question_number]
    updated_questions.pop(question_number)
    print(question)
    for que,ans in total:
        if que==question:
            answer=input("Enter answer : ")
            if answer.lower()==ans:
                score+=1
            else:
                continue 

print(f"your score is {score}")               
                    

