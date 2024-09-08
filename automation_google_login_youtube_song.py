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
pyautogui.typewrite("www.youtube.com")
pyautogui.typewrite('\n')
time.sleep(5)

'''pyautogui.moveTo(195,470)
pyautogui.click()
time.sleep(5)

pyautogui.moveTo(595,305)
pyautogui.click()
time.sleep(5)'''

pyautogui.moveTo(452,187)
pyautogui.click()
time.sleep(5)

pyautogui.typewrite("Bollywood songs")
pyautogui.click()
pyautogui.sleep(5)

pyautogui.moveTo(228,437)
pyautogui.click()
pyautogui.sleep(10)
pyautogui.moveTo(653,496)
pyautogui.click()
pyautogui.sleep(2)







