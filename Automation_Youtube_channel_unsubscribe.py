import pyautogui
import time
# Wait for 5 seconds to ensure the browser is open
time.sleep(5)

# Move the mouse to the email input field and click
pyautogui.moveTo(386, 123)  # Adjust the coordinates to match your screen
pyautogui.click()

# Type the email address
pyautogui.typewrite('https://accounts.google.com/signin')
pyautogui.typewrite('\n')
time.sleep(10)


pyautogui.moveTo(523,517)
#pyautogui.click()
pyautogui.typewrite('priyanktyagi011@gmail.com')
pyautogui.typewrite('\n')
time.sleep(5)

        #pyautogui.click()
pyautogui.typewrite('Password')
pyautogui.typewrite('\n')
time.sleep(5)

pyautogui.moveTo(386,123)
pyautogui.click()
        #pyautogui.typewrite('Youtube')
pyautogui.typewrite("https://www.youtube.com/watch?v=Zj1mksQXKSk")
pyautogui.typewrite('\n')
time.sleep(5)
pyautogui.moveTo(431,853)
pyautogui.click()
print("channel sussesfully subscribed")
pyautogui.moveTo(527,788)
pyautogui.click()
pyautogui.moveTo(570,635)
pyautogui.click()
print("channel sussesfully Unsubscribed")
        