def mood_bot():
    print("🤖 AI Bot: Hi! I am your mood assistant 😊")

    mood = input("How are you feeling today? (good/bad): ").lower()

    if mood == "good":
        print("🤖 AI Bot: That's amazing! 🌟")
        print("Keep smiling and enjoy your day!")

        activity = input("Want a fun suggestion? (yes/no): ").lower()

        if activity == "yes":
            print("🤖 AI Bot: Try listening to music, going for a walk, or learning something new 🎵")

        else:
            print("🤖 AI Bot: No problem! Have a wonderful day 😊")


    elif mood == "bad":
        print("🤖 AI Bot: I'm sorry you are feeling that way 💙")
        print("Remember, difficult moments don't last forever.")

        choice = input("Would you like a motivation message? (yes/no): ").lower()

        if choice == "yes":
            print("🤖 AI Bot: You are stronger than your problems. Take things one step at a time 🌱")

        else:
            print("🤖 AI Bot: That's okay. I hope you feel better soon ❤️")


    else:
        print("🤖 AI Bot: I didn't understand. Please type only good or bad.")


mood_bot()