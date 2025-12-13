print("Hello! I'm AI Bot. What's your name?")
name=input
print(f"Nice to meet you{name}")
print("How are you feelig today?:good/bad")
if mood=="good":
    print("I'm glad to hear that.")
elif mood =="bad":
    print("I'm so sorry to hear that.")
else :
    print("I see it is sometimes hard to put feelings into words.")
print(f"It was nice catting with you, {name}")