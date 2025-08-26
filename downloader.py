import pyautogui
import time

couter = 0
number = 0

print("Make sure you a singular browser window with ONLY the OneDrive tabs open, in the order you want to download the slides, left to right. Then, use your browser to see how many tabs you have open. Enter this below.")
print("Enter the number: ")

number = int(input())

print("You have entered: " + str(number) + " tabs. The script will now start downloading the slides.")
print("You have 4 seconds to switch to the browser window.")

time.sleep(4) # allows user to select to browser window

while couter < number:
    # Click OneDrive download (fixed position)
    time.sleep(1000)
    pyautogui.click(x=24, y=121)  # Check this
    print("Clicked download button for tab " + str(couter + 1))
    time.sleep(3)
    
    # Close tab
    pyautogui.hotkey('command', 'w')
    time.sleep(1)
    
    couter += 1

print("All downloads have been clicked. Please check your downloads folder for the files.")
print("This little script was made by James Coates, whom was sick of downloading all slides one by one from the course website manually, for the UNSW COMP1531 course. If you have any issues, please contact me at james@coatesy.au")
