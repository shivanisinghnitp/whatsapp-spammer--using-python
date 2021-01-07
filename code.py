#run this code in jupyter notebook
import pyautogui
import webbrowser as wb
import time
wb.open("web.whatsapp.com")
time.sleep(30)
for i in range(100):
    pyautogui.press("H")
    pyautogui.press("E")
    pyautogui.press("L")
    pyautogui.press("L")
    pyautogui.press("O")
    pyautogui.press("enter")
