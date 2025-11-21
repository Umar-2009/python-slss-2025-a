# version 1
def vote_listed_choices():
    """Display all choices
    5 users vote for their choice
    Results will be printed"""


CHOICES = [
    "A. Blenz",
    "B. BubbleQueen",
    "C. SunTea",
    "D. Heytea",
    "E. Coco",
    "F. FreshT",
]
#bucket for votes
Blenz = 0
BubbleQueen = 0
SunTea = 0
Heytea = 0
Coco = 0
FreshT = 0
spoiled_votes = 0

# show all choices
print("Vote for your favourite from the list. ")
print("Give the letter of your choice")
for choice in CHOICES:
    print(choice)
# ask user for their choice
vote = input("Your Vote").strip(".,/?!")
# keep track with tally
if vote == "a":
    Blenz = Blenz +1
elif vote == "b":
    BubbleQueen += 1
elif vote == "c":
    SunTea += 1
elif vote == "d":
    Heytea += 1
elif vote == "e":
    Coco += 1
elif vote == "f":
    FreshT += 1
else:
    spoiled_votes += 1
# data analysis
# give raw score
print("Voting Results ---")
print(f"Blenz: {Blenz} votes")
print(f"Bubble Queen: {BubbleQueen} votes")
print(f"Sun Tea: {SunTea} votes")
print(f"hey tea: {Heytea} votes")
print(f"CoCo: {Coco} votes")
print(f"Fresh T: {FreshT} votes")
print(f"Spoiled votes: {spoiled_votes} votes")
# give score as percentage
print("Vote share percentage ---")
    total = Blenz + BubbleQueen + SunTea + Heytea + Coco + FreshT + spoiled_votes
    print(f"Blenz: {Blenz / total * 100} %")
    print(f"Bubble Queen: {BubbleQueen / total * 100} %")
    print(f"Sun Tea: {SunTea / total * 100} %")
    print(f"hey tea: {Heytea / total * 100} %")
    print(f"CoCo: {Coco / total * 100} %")
    print(f"Fresh T: {FreshT / total * 100} %")
    print(f"Spoiled votes: {spoiled_votes / total * 100} votes")

def main():
    vote_listed_choices()


if __name__ == "__main__":
    main()

# version2
# ask user for favourite boba place
# keep tally
# data analysis
# give raw scores
# give socres a s a percentage
