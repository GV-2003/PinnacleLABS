import time
import datetime
import threading
import sys

#  Windows sound 
try:
    import winsound
    WINDOWS = True
except ImportError:
    WINDOWS = False


def play_tone(tone_choice, duration=1000):
    """Play selected alarm tone"""
    if WINDOWS:
        if tone_choice == 1:
            winsound.Beep(800, duration)
        elif tone_choice == 2:
            winsound.Beep(1200, duration)
        elif tone_choice == 3:
            winsound.Beep(600, duration)
    else:
        print("\a" * 5)
        time.sleep(1)


def alarm_clock(alarm_time, tone_choice, snooze_minutes):
    print(f"\n Alarm set for {alarm_time}")
    
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        if current_time == alarm_time:
            print("\n WAKE UP!")

            # Play alarm 
            while True:
                play_tone(tone_choice)
                choice = input("Type 's' to snooze or 'x' to stop: ").lower()

                if choice == "s":
                    snooze_time = datetime.datetime.now() + datetime.timedelta(minutes=snooze_minutes)
                    alarm_time = snooze_time.strftime("%H:%M")
                    print(f"Snoozed until {alarm_time}")
                    break
                elif choice == "x":
                    print("Alarm stopped. Have a great day!")
                    return

        time.sleep(20)


def main():
    print("=== Python Alarm Clock ===")

    alarm_time = input("Set alarm time (HH:MM, 24-hour format): ")

    print("\nChoose alarm tone:")
    print("1. High beep")
    print("2. Medium beep")
    print("3. Low beep")
    tone_choice = int(input("Enter tone number (1-3): "))

    snooze_minutes = int(input("Snooze duration (minutes): "))

    alarm_thread = threading.Thread(
        target=alarm_clock,
        args=(alarm_time, tone_choice, snooze_minutes)
    )
    alarm_thread.start()


if __name__ == "__main__":
    main()
