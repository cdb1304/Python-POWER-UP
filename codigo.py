import pyautogui
import time

pyautogui.PAUSE = 0.8

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

pyautogui.hotkey("ctrl", "l")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press ("enter")

time.sleep(1)

pyautogui.PAUSE = 0.5
pyautogui.click(x=801, y=371)
pyautogui.write("cauabap@gmail.com")
pyautogui.click(x=717, y=471)
pyautogui.write("Caua13bap")
pyautogui.click(x=967, y=579)
pyautogui.rightClick