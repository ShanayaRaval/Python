# 1 Import clorama
from colorama import Fore, Style
from textblob import TextBlob

# 4 Initializing colorama for coloured output
colorama.init()

# 7 Begin with the start of the program
print(Fore.CYAN + "Welcome to Sentiment Spy!")
# 10 Request the user's name
 user_name = input(Fore.MAGENTA + "Please say your name: " + Style.RESET_ALL).strip()
# 12 If not user_name:
if not user_name:
    user_name = "Mystery Agent" # Fallback if user doesn't provide a name

# 15 Start conversation and a list of tuples: (text, polarity, sentiment_type)
conversation_history = []

# 18 Print instructions
print(f"{Fore.CYAN}Hello, Agent {user_name}!{Style.RESET_ALL}")
print(f"{Fore.CYAN}Type a sentence and I will analyze your sentence with TextBlob and show you the sentiment. {Style.RESET_ALL}")
print(f"{Fore.CYAN}Type {Fore.YELLOW}\"history\"{Fore.CYAN} to see past analyzed inputs.{Fore.CYAN}")
print(f"{Fore.CYAN}Type {Fore.YELLOW}\"exit\"{Fore.CYAN} to quit.{Style.RESET_ALL}")

# 23 Main program loop
while True:

    user_input = input(f"{Fore.GREEN}>> {Style.RESET_ALL}").strip()

    # 27 If not user_input:
    if not user_input:
        print(f"{Fore.RED}Please enter some text or a valid command.{Style.RESET_ALL}")
        continue

    # 32 Check for commands
    # 33 If user input is "exit":
    if user_input.lower() == "exit":
        print(f"{Fore.BLUE}Exiting Sentiment Spy. Farewell, Agent {user_name}! {Style.RESET_ALL}")
        break

    # 37 If user input is "clear":
    elif user_input.lower() == "clear":
        conversation_history.clear()
        print(f"{Fore.CYAN}All conversation history cleared!{Style.RESET_ALL}")
        continue

    # 43 If user input is "history":
    elif user_input.lower() == "history":
        if not conversation_history:
            print(f"{Fore.YELLOW}No conversation history yet.{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN}Conversation History:{Style.RESET_ALL}")
            # 47 Iterate through conversation_history, get index, text, and sentiment_type
            for idx, (text, polarity, sentiment_type) in enumerate(conversation_history, start=1):
                # 49 Choose color and emoji based on sentiment
                if sentiment_type == "Positive":
                    color = Fore.GREEN
                    emoji = "😀"
                elif sentiment_type == "Negative":
                    color = Fore.RED
                    emoji = "🙁"
                else: # Neutral
                    color = Fore.YELLOW
                    emoji = "😐"

                # 58 Print history item
                print(f"[{idx}]. {color}{emoji} {text} ({sentiment_type}) {Style.RESET_ALL}")
            continue

    # 62 Analyze sentiment
    polarity = TextBlob(user_input).sentiment.polarity
    if polarity > 0.05:
        sentiment_type = "Positive"
        color = Fore.GREEN
        emoji = "✅"
    elif polarity < -0.05:
        sentiment_type = "Negative"
        color = Fore.RED
        emoji = "❌"
    else:
        sentiment_type = "Neutral"
        color = Fore.YELLOW
        emoji = "➖"

    # 78 Store in history
    conversation_history.append((user_input, polarity, sentiment_type))

    # 81 Print result with color, emojis, and polarity
    print(f"{color}{emoji} {sentiment_type} sentiment detected!{Style.RESET_ALL}")
    print(f"{Fore.CYAN} (Polarity: {polarity}){Style.RESET_ALL}")