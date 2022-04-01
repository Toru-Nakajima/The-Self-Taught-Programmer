my_character ={"height": "170",
               "favorite calor": "green",
               "favorite author": "Atul Gawande"}

answer = input("type any key-name:")

if answer in my_character:
    print(my_character[answer])
else:
    print("You can't find the name.")

