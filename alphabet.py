import time
import keyboard

def type_key(letter):
    keyboard.press_and_release(letter)

if __name__ == "__main__":
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    print("sleeping for 3 seconds")
    time.sleep(3)
    for char in alphabet:
        time.sleep(0.0001)
        type_key(char)
