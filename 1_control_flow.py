statement_one = (2 + 2 + 2 >= 6) and (-1 * -1 < 0)

statement_two = (4 * 2 <= 8) and (7 - 1 == 6)

credits = 120
gpa = 3.4


if (credits >= 120) and (gpa >= 2.0):
  print("You meet the requirements to graduate!")

# not
if not (credits >= 120) and not (gpa >= 2.0):
  prin("You do not have enough credits to graduate."
)


# else
if (credits >= 120) and (gpa >= 2.0):
  print("You meet the requirements to graduate!")
else:
  print("You do not meet the requirements to graduate.")

# elif
grade = 86

if(grade >= 90):
  print('A')
elif(grade >= 80):
  print('B')
elif(grade >= 70):
  print('C')
elif(grade >= 60):
  print('D')
else:
  print('F')