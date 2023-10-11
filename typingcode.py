import time
import pyperclip
import keyboard

current_text = ''

def type_slowly(text, interval=0.01):  # Set delay to 0.11 seconds
    # Press the 'enter' key 100 times
    for _ in range(100):
        keyboard.press('enter')
        keyboard.release('enter')
        time.sleep(0.01)

    # Press the 'up' key 100 times to return to the original position
    for _ in range(100):
        keyboard.press('up')
        keyboard.release('up')
        time.sleep(0.01)

    for char in text:
        # If there's a change in the copied text while typing, stop input
        if current_text != text:
            break
        if char == '\n':
            keyboard.press('right')  # Press the '→' key to move to the beginning of the next line
            keyboard.release('right')
            #time.sleep(0.01)
        else:
            keyboard.write(char)  # Using keyboard.write() which might be faster

        time.sleep(interval)  # Wait for the specified interval before next input


def main():   # 
    global current_text
    typing = False

    while True:
        if keyboard.is_pressed('esc'):  # Check if the 'Esc' key is pressed
            break  # Exit the loop and end the program

        if keyboard.is_pressed('ctrl+c') and not typing:
            time.sleep(0.10)  # Wait for the change in keyboard state
            current_text = pyperclip.paste()

        if keyboard.is_pressed('ctrl+m') and not typing:
            typing = True
            type_slowly(current_text)
            typing = False
        

if __name__ == "__main__":
    main()
