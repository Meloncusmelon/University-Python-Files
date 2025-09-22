Class= ["Math", "English", "Science", "History", "Art" ]
Math= [85, 90, 70 ]
English= [78, 82, 65 ]
Science= [92, 85, 60 ]
History= [88, 80, 75 ]
Art= [76, 90, 72 ]
Students = [ "Alice", "Bob", "Charlie" ]
Alice = [85, 78, 92, 88, 76]
Bob = [90, 82, 85, 80, 90]
Charlie = [70, 65, 60, 75, 72]
# Calculate averages
Aliceaverage = sum(Alice) / len(Alice)
Bobaverage = sum(Bob) / len(Bob)
Charlieaverage = sum(Charlie) / len(Charlie)
Classaverage = (Aliceaverage + Bobaverage + Charlieaverage) / 3
averages = [Aliceaverage, Bobaverage, Charlieaverage]
highest = max(averages)
lowest = min(averages)
print("Class Average:", Classaverage)
print("Highest average:", highest)
print("Lowest average:", lowest)
