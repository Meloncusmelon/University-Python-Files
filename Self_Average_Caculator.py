Maths= int(input("Enter your Maths score: "))
English= int(input("Enter your English score: "))
Science= int(input("Enter your Science score: "))
History= int(input("Enter your History score: "))
Art= int(input("Enter your Art score: "))
average= (Maths + English + Science + History + Art) / 5
print("Your average score is:", average)
if average >= 90:
    print("Grade: A")
elif average >= 80:
    print("Grade: B")
elif average >= 70:
    print("Grade: C")
elif average >= 60:
    print("Grade: D")
elif average >= 50:
    print("Grade: E")
else:
    print("Grade: F")
    