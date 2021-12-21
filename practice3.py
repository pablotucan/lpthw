import statistics

def higher_wam(wam1, wam2):
    if wam1 > wam2:
        print(f"{Person1} has a higher WAM than {Person2}!")
    if wam1 < wam2:
        print(f"{Person2} has a higher WAM than {Person1}!")
    if wam1 == wam2:
        print(f"{Person2} has the same WAM as {Person1}!")

print("Hello welcome to WAM competition!!!!")

Person1 = input("What's the first competitors name? ")
Person2 = input("What's the second competitors name? ")

print("Thank you!")

p1s = input(f"Okay, {Person1} what was your first subject? ")
p1_2s = input("And what was your second subject? ")
p1_3s = input("Third subject? ")
p1_4s = input("Finally, what was your fourth subject? ")

print("Great, now let's move on to grades")

subject1_1 = int(input(f"What is {Person1}'s grade in {p1s}? "))
subject1_2 = int(input(f"What is {Person1}'s grade in {p1_2s}? "))
subject1_3 = int(input(f"What is {Person1}'s grade in {p1_3s}? "))
subject1_4 = int(input(f"What is {Person1}'s grade in {p1_4s}? "))

subject1_total = [subject1_1, subject1_2, subject1_3, subject1_4]

wam1 = statistics.mean(subject1_total)

p2s = input(f"Okay now {Person2}'s turn, what was your first subject? ")
p2_2s = input("And what was your second subject? ")
p2_3s = input("Third subject? ")
p2_4s = input("Finally, what was your fourth subject? ")

print("Great, now let's move on to grades")

subject2_1 = int(input(f"What is {Person2}'s grade in {p2s}? "))
subject2_2 = int(input(f"What is {Person2}'s grade in {p2_2s}? "))
subject2_3 = int(input(f"What is {Person2}'s grade in {p2_3s}? "))
subject2_4 = int(input(f"What is {Person2}'s grade in {p2_4s}? "))

subject2_total = [subject2_1, subject2_2, subject2_3, subject2_4]

wam2 = statistics.mean(subject2_total)

higher_wam(wam1, wam2)
