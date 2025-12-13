print("Hello! I am AI Bot. What's your name? ")
name = input ()
print(f'Nice to meet you,{name}')
print('How are you feeling today? good/bad')
mood = input().lower()
if mood=='good':
    print('I am glad to hear that.')
elif mood=='bad':
    print("I am sorry to hear that.")
else :
    print("I see it is sometimes hard to put feelings into words")
print(f"It was nice chatting with you {name}")