# Ex1:
text = input("Enter your text: ")
for char in range(len(text)):
    print(text[char])

# Ex2:
text = input("Enter your text: ")
for i in range(len(text)):
    print(i)

# Ex3:
text = input("Enter your text: ")
isFound = False
for i in text:
    if i.isupper():
        isFound = True
if isFound:
    print("Yes")
else:
    print("No")

# Ex4:
text = "3 4 5 6 "
new_text = ""
sum = 0
for char in text:
    if char != ' ':
        print(char)
        new_text += char
        sum += int(char)
print(new_text)
print(sum)

# Ex5:Q1
text = "454639"
count_odd = 0
count_even = 0
for char in text:
    if int(char) % 2 == 0:
        count_even +=1
    else:
        count_odd +=1
print("even number", "=", count_even)
print("odd number", "=", count_odd)

# Ex5:Q2
text = "454639"
sum = 0
for char in text:
    sum += int(char)
print(sum)

# Ex5:Q3
text = "454639"
sum = 0
for char in text:
    if int(char) % 2 == 0:
        sum += int(char)
print(sum)

# Ex6:
num = int(input("Enter your number: "))
if num % 2 == 1:
    print("Odd")
else:
    print("Even")

# Ex7:
isFound = False
while not isFound:
    num = int(input("Enter your num: "))
    if num >= 10 and num <= 20:
        print("Contiue")
    else:
        isFound = True
print("Out of range")

# Ex8:Q1
text = "9394884039"
count8 = 0
for i in range(len(text)):
    if text[i] == "8":
        count8 +=1
print("number_8", "=", count8)

# Ex8:Q2
text = "9394884039"
isFound = False
i = 0
while not isFound:
    if text[i] == "8":
        isFound = True
        print(i)
    i +=1

# Ex9:Q1
text = "3 4 5 6 "
new_text = ""
for char in text:
    if char != ' ':
        new_text += char
print(new_text)

# Ex9:Q2
text = "3 4 5 6 "
for char in text:

# Ex10:
max = 0
min = 0
for i in range(5):
    number = int(input("Enter your num: "))
    if number > max:
        max = number
    elif number < min:
        min = number
print("max", max)
print("min", min)
