import pyautogui as pag
import time

print(pag.size())

time.sleep(2)
print(pag.position())

pag.moveTo(100,200)
pag.moveTo(1000,1000,5) # 5초동안 좌표로 이동
pag.click()
pag.click(button='right')
pag.doubleClick()
pag.click(clicks=3,interval=1) # 3번클릭 1초마다

pag.dragTo(400,200,2)

pag.typewrite('Hello world!', interval=0.1)
pag.hotkey('ctrl','c')
pag.keyDown('c')
pag.keyUp('c')

pag.press('c')

pag.screenshot()
pag.screenshot('scr.png')
pag.screenshot('scr.png',region=(0,0,300,300))

coord = pag.locateOnScreen('scr.png')
center = pag.center(coord)

center = pag.locateCenterOnScreen('scr.png')
pag.click(center)

alert = pag.alert()
print(alert)

confirm = pag.confirm('shall i proceed?')
print(confirm)

button = pag.confirm('click option button', buttons=['A','B','C'])

if button == 'A':
    print('A')
if button == 'B':
    print('B')
else:
    print('C')


user_input = pag.prompt('Enter your input')
print(user_input)

user_pw = pag.password('Enter your hidden input')
print(user_pw)

pag.PAUSE = 0.05

'''
['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
'8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
'browserback', 'browserfavorites', 'browserforward', 'browserhome',
'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
'command', 'option', 'optionleft', 'optionright']
'''