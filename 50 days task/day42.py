### # TASK 1 ####

# from textblob import Word

# def spelling_checker():
#     while True:
#         word = input("Enter a word: ")
#         if Word(word).spellcheck()[0][0] == word:
#             return word
#         else:
#             suggestion = Word(word).spellcheck()[0][0]
#             response = input(f"Did you mean '{suggestion}'? (yes/no): ")
#             if response.lower() == "yes":
#                 return suggestion

# # Test the function
# correct_word = spelling_checker()
# print(f"Correct word: {correct_word}")


###### ### TASK 2  ####### ####


import datetime
import time
import winsound

def alarm():
    alarm_hour = int(input("Enter the hour for the alarm (0-23): "))
    alarm_minute = int(input("Enter the minute for the alarm (0-59): "))

    current_time = datetime.datetime.now()
    alarm_time = current_time.replace(hour=alarm_hour, minute=alarm_minute, second=0, microsecond=0)

    print(f"Alarm set for: {alarm_time.strftime('%H:%M')}")

    while True:
        current_time = datetime.datetime.now()
        if current_time >= alarm_time:
            print("Alarm time reached!")
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
            break

        # Sleep for a short duration to avoid continuous checking
        # and reduce CPU usage
        time.sleep(1)

# Call the alarm function
alarm()


