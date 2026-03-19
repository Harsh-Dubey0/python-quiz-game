import json
import random



print("====================================")
print("        🧠 QUIZ CHALLENGE 🧠")
print("====================================")
print("📚 Test your knowledge")
print("🎯 Earn bonus for correct streaks")
print("⚠️  Avoid penalties for wrong streaks")
print("====================================")

input("\nPress Enter to start the game...")



with open(r"quiz_questions.json", "r") as file:
    questions = json.load(file)


total_questions = len(questions)
print(f"\nTotal questions available: {total_questions}")
num = int(input("How many questions do you want to play? "))
if num > total_questions:
    print("You entered more than available questions.")
    num = total_questions
    
selected_questions= random.sample(questions,num)
score = 0
correct_streak = 0
wrong_streak = 0

correct_count = 0
wrong_count = 0
bonus_count = 0
penalty_count = 0

for q in selected_questions:
    print("\n", q["question"])
    
    for i, option in enumerate(q["options"], 1):
        print(f"{i}. {option}")
        
    user = int(input("Enter option number: "))
    
    if q["options"][user-1] == q["answer"]:
        print("✅ Correct")
        score += 10
        correct_streak += 1
        wrong_streak = 0
        correct_count+=1
        
        if correct_streak == 5:
            print("🎉 Bonus +20")
            score += 20
            correct_streak = 0
            bonus_count+=1
    else:
        print("❌ Wrong")
        score -= 10
        wrong_streak += 1
        correct_streak = 0
        wrong_count+=1
        
        if wrong_streak == 3:
            print("⚠️ Penalty -20")
            score -= 20
            wrong_streak = 0
            penalty_count+=1
            
            
print("\n==========================================")
print("           🧠 QUIZ CHALLENGE 🧠")
print("              GAME RESULTS")
print("==========================================")

print("Total Questions Played :", num)
print("Correct Answers        :", correct_count)
print("Wrong Answers          :", wrong_count)
print("Bonus Earned           :", bonus_count)
print("Penalty Applied        :", penalty_count)
print("Final Score            :", score)

print("==============================")
print("🎮 Thanks for playing!")
