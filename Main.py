import random
subjects = ["Akshay kumar","M.S.Dhoni","A naughty monkey","A cab driver from Mumbai","A dancing cat"]
actions = ["eats","sings","plays","studies","cry"]
places = ["In filmcity","In the stadium","at Amer fort","at ganga ghat","in the jungle"]

while True:
    subject=random.choice(subjects)
    actions=random.choice(actions)
    places=random.choice(places)

    headline=f"BREAKING NEWS: {subject} {actions} {places}"
    print("\n" + headline)

    user_input=input("\nDo you want another headline? (yes/no)").strip().lower()
    if user_input != "yes":
        break

print("\nThank you for using the Fake News Headline Generator.Have a fun day!")