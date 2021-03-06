#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

welcome = "Welcome to the tip calculator."
print(welcome)

total = input("What was the total bill? $") #$150
total = float(total)

percent = input("What percentage tip would you like to give? 10, 12, or 15? ") #10
percent = int(percent) #don't want any decimal pionts
percent /= 100

people = input("How many people to split the bill? ") #2
people = int(people)

per_person = (total * percent + total) / people
per_person = round(per_person, 2)
per_person = "{:.2f}".format(per_person) #limit a float to two decimal places

result = f"Each person should pay: ${per_person}" #used a f-string to add a string and an float

print(result)