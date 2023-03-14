janExp=int(input("Expense for Jan: "))
febExp=int(input("Expense for Feb: "))
marExp=int(input("Expense for Mar: "))
aprExp=int(input("Expense for Apr: "))
mayExp=int(input("Expense for May: "))
junExp=int(input("Expense for Jun: "))
julExp=int(input("Expense for Jul: "))
augExp=int(input("Expense for Aug: "))
sepExp=int(input("Expense for Sep: "))
octExp=int(input("Expense for Oct: "))
novExp=int(input("Expense for Nov: "))
decExp=int(input("Expense for Dec: "))

expenseEachMonth=[janExp,febExp,marExp,aprExp,mayExp,junExp,julExp,augExp,sepExp,octExp,novExp,decExp]

total=0

for items in expenseEachMonth:
    total=total+items

print("The total expense for the year is",total)