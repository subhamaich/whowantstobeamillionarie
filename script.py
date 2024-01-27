import numpy
data = {
    "1. What is the capital of India?": "New Delhi",
    "2. What is the capital of West Bengal?": "Kolkata",
    "3. What is the capital of Maharashtra?": "Mumbai",
    "4. What is the capital of Assam?": "Dispur",
    "5. What is the capital of Tripura?": "Agartala",
    "6. What is the capital of Gujarat?" : "Gandhinagar",
    "7. What is the capital of Uttar Pradesh?": "Lucknow",
    "8. What is the capital of Bihar?": "Patna",
    "9. What is the capital of Rajasthan?": "Jaipur",
    "10. What is the capital of Tamil Nadu?": "Chennai"
}

options = {
    "A": ["New Delhi", "Mumbai", "New Delhi", "Dispur", "Lucknow", "Shimla", "Patna", "Kolkata", "Jaipur", "Shimla"],
    "B": ["Mumbai","Kolkata", "Chennai", "Agartala", "Agartala", "Jaipur", "Lucknow", "Lucknow", "Patna", "Kolkata" ],
    "C": ["Kolkata","New Delhi", "Kolkata", "Shilong", "Patna", "Gandhinagar", "Jaipur", "Patna", "Shimla", "Bangalore" ],
    "D": ["Chennai","Chennai", "Mumbai", "Patna", "Shimla", "Chennai", "Chennai", "Chennai", "Chennai", "Chennai" ]
}

print("There will be ten questions. If you answer one wrong, you're out.")
print("The prizes are as follows:\n ")
score = 0
cash = 0
count = 0

for key, value in data.items():
    print(key)
    
    for i,j in options.items():
        print(i+". "+j[count])
    inp = input("Enter option:").upper()
    answer = ""
    while inp not in options.keys():
         print("Enter correct option")
         inp = input("Enter option:").upper()
    if inp in options.keys():
        answer = options[inp][count]
        print(data[key])
        if answer == data[key]:
            print("Correct")
            score += 10
            print(score)
            count += 1
        else:
            print("You're out!")
            break
            
    
    

if score >= 100:
     cash = 10000000
elif score >= 60:
     cash = 5000000
elif score >= 30:
     cash = 1000000

print("You won "+str(cash)+" dollars.")
