age_now = int(input("How old are you now? "))
age_2049 = age_now + 31
print(f"In 2049 you will be {age_2049} years old!")

score1 = float(input("Judge 1: "))
score2 = float(input("Judge 2: "))
score3 = float(input("Judge 3: "))
score4 = float(input("Judge 4: "))
score5 = float(input("Judge 5: "))

average = (score1 + score2 + score3 + score4 + score5) / 5

print(f"Your Olympic score is {average:.1f}")

burger = input("Would you like a burger for $5? (Yes/No) ").lower()
fries = input("Would you like fries for $3? (Yes/No) ").lower()

total = 0

if burger == "yes":
    total += 5
if fries == "yes":
    total += 3

total_with_tax = total * 1.14

print(f"Your total is ${total_with_tax:.2f}")
