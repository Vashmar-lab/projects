name = input("Type your name: ")
print("Welcome", name, "to this adventure")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way you want to go? ").lower()

if answer == "left":
    answer == input("You come to a river, you can walk around or you can swim across? Type walk to walk around and swim to swim accross: ").lower()

    if answer == "swim":
        print("You swam across and were eaten by an alligator")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game")
    else:
        print("Not a valid option. You lose")

elif answer == "right":
    answer = input("You come to a bridge, do you want to cross it or head back? (cross/back) ")

    if answer == "back":
        print("You go back to the main road")
    elif answer == "cross":
        answer = input("You crossed the bridge and you met a stranger, would you talk to them? (Yes/No) ")
            
        if answer == "Yes":
            print("You talk to the stranger and they give you a Gold. You WIN!")
        elif answer == "No":
            print("You ignore the stranger and they are offended and You LOSE!")
        else:
            print("Not a valid option. You lose")
    else:
        print("Not a valid option. You lose")

else:
    print("Not a valid option. You lose")

print("Thank You for trying", name)