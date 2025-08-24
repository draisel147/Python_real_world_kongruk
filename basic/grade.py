grade = int(input("ป้อนคะแนนของคุณ : "))

if grade >= 80 and grade <= 100:
    grade = "A"
elif grade >= 70 and grade <= 79:
    grade = "B"
elif grade >= 0 and grade <= 69:
    grade = "F"
else:
   grade = "N (Invalid)"

print(f"เกรดของคุณคือ {grade}")
