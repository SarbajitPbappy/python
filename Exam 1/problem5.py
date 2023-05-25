import pyautogui
numOFline=int(input())
for i in range(0,numOFline):
    line=""
    for j in range(0,i+1):
        line+="#"
    pyautogui.typewrite(line)
    pyautogui.typewrite("\n")