# -*- coding: utf-8 -*-
"""Internal_Assessment1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mWamxFVBkwlIHe6vaTvm4Q00KDJeG5CP
"""

#1
a = float(input("Enter length in meters : "))
b = float(input("Enter breadth in meters : "))

c = a *b

if c > 1500:
  print("The property is large with an area of {} ".format(c))
elif c > 750:
  print("The property is medium with an area of {} ".format(c))
else:
  print("The property is small with an area of {} ".format(c))

#2
a = float(input("Enter height in meters : "))
b = float(input("Enter weight in kgs : "))

BMI = b/(a**2)

print("Your BMI is {} for the height {}m and weight of {}kg ".format(BMI,a,b))

#3
def add():
  b = int(input("Enter total count of students to add"))
  for i in range(len(record)+1,len(record)+b+1):
    c = input("Enter subject : ")
    d = input("Enter grade : ")
    record[i]={c:d}
  print(record)

def update():
  e = int(input("Enter student id : "))
  if e in record:
    f = input("Enter subject : ")
    g = input("Enter grade : ")
    record[e] = {f:g}
    print(record)
  else:
    print("No student in the given id, please enter correct id!")
    exit

print("Select an option")
print("A. New record")
print("B. Existing record")
opt = input("Select A or B : ")

if opt =='A':
  record =dict()
else:
  if record == {}:
    print("No exisiting record, creating new record!")
    record = dict()

print("Select an option")
print("1. Add")
print("2. Update")
print("3. Retrive")
print("4. Exit")
a = int(input("Enter the option : "))

if a == 1:
  add()
elif a == 2:
  update()
elif a == 3:
  print(record)
elif a == 4:
  exit
else:
  print("Please select valid option!!")
  exit

#4
a = int(input("Enter age : "))

if a < 8:
  print("You are {} years old, so child categories will be recommended".format(a))
elif a < 18 and a >= 8:
  print("You are {} years old, so teen categories will be recommended".format(a))
elif a > 18 and a<= 40:
  print("You are {} years old, so adult categories will be recommended".format(a))
else:
  print("You are {} years old, so senior categories will be recommended".format(a))

#5
a = []
existing_id = [1,2,3,4,5,6,7,8,9,10]
for i in range(len(existing_id)):
  if existing_id[i]%2 == 0:
    a.append(existing_id[i])
# print("Even id's : {}".format(a))
c = input("Type message to be sent : ")
print("The message '{}' has been sent to {}".format(c,a))

#6
passwords = {'user1':'password1','user2':'password2'}

def enter_details():
  a = input("Enter user id : ")
  b = input("Enter user id : ")

  if passwords[a] == b:
    print("Your approved")
    exit
  else:
    enter()

def enter():
  enter_details()

enter()

#7
print("Select an option")
print("A. Add feedback")
print("B. View feedback")
opt = input("Select A or B : ")

if opt == 'A':
  feedback = dict()
  a = int(input("Enter total count of feedback : "))
  for i in range(a):
    feedback[i] = int(input("Enter score on range of 1 to 5 :"))

  scores = feedback.values()
  total_score = 0
  for i in scores:
    total_score = total_score+i
  avg = int(total_score//len(scores))
  if avg == 5:
    print("Excellent")
  elif avg >=3 and avg <5:
    print("Average")
  else:
    print("Bad")
  exit
else:
  if feedback == {}:
    print("No exisiting feedback, creating new feedback!")
    feedback = dict()
    a = int(input("Enter total count of feedback : "))
    for i in range(a):
      feedback[i] = int(input("Enter score on range of 1 to 5 :"))

    scores = feedback.values()
    total_score = 0
    for i in scores:
      total_score = total_score+i
    avg = int(total_score//len(scores))
    if avg ==5:
      print("Excellent")
    elif avg >=3 and avg <5:
      print("Average")
    else:
      print("Bad")
    exit
  else:
    exit

#8
a = input("Enter comment :")
c = 0
vowels = ['a','e','i','o','u','A',"E",'I',"O","U"]
for i in a:
  if i in vowels:
    c = c+1
print("Total vowels in the comments is {}".format(c))

#9

#10
def calculate_loan():
  a = int(input("Enter loan amount : "))
  b = int(input("Enter total year : "))
  if b > 10:
    c = 0.15
  if b >=5 and b<=10:
    c = 0.1
  else:
    c= 0.05
  loan = a*b/(c*100)
  print("Total loan: {}".format(a+loan))

def calculate_savings():
  a = int(input("Enter savings amount : "))
  b = int(input("Enter total year : "))
  if b > 10:
    c = 0.10
  if b >=5 and b<=10:
    c = 0.07
  else:
    c= 0.03
  savings = a*b/(c*100)
  print("Total savings: {}".format(a+savings))

print("Select an option")
print("A. Check loan")
print("B. Check Savings")
opt = input("Select A or B : ")

if opt == 'A':
  try:
    calculate_loan()
    print("This is your total loan amount to be paid")
  except:
    print("Please enter valid value!!!")
elif opt == 'B':
  try:
    calculate_savings()
    print("This is your total savings amount")
  except:
    print("Please enter valid value!!!")

#11
a= []
def poll_vote():
  b = int((input("Enter voter id : ")))
  if len(str(b)) == 6:
    c = int(input("Enter party id : "))
    if len(str(c)) ==1 and c <10 and c>0:
      a.append(c)

try:
    poll_vote()
    print("Your poll has been recorded")
except:
    print("The details you entered is wrong!!!."+'\n'+"Please enter valid details")

#12
a = int(input("Enter value : "))
b = int(input("Enter value to be divided : "))

try :
  c = a/b
  print("Output {}".format(c))
except:
  print("Cant divide by zero")

#13
a = input("Enter date :")
b = input("Enter uptime : ")

file = open('/content/uptime_reports.txt','w')
if not file:
  file.writeline('\n'+"The total uptime is {} on {}".format(b,a))
else:
  file.write("The total uptime is {} on {}".format(b,a))
file.close()
file = open('/content/uptime_reports.txt','r')
print(file.read())
file.close()

#14
file = open('/content/uptime_reports.txt','r')
print(file.read())
file.close()

#15
file = open('/content/uptime_reports.txt','r')
content=file.read()
file.close()
file = open('/content/uptime_reports.txt','w')
a = input("Enter date :")
b = input("Enter uptime : ")
file.write(content+'\n'+"The total uptime is {} on {}".format(b,a))
file.close()
file = open('/content/uptime_reports.txt','r')
print(file.read())
file.close()