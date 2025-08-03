import keyboard as k
import pyautogui as py
import time as t

p = print

wlacz = 'x'         # Aktywacja
wyjscie = '='       # De-aktywacja
delay = 0.01         # Delay przed zmiana

def jasnysad(event):
    if event.name == wlacz and event.event_type == 'down':
        sw, sh = py.size()
        s_x, s_y = sw // 2, sh // 2
        
        op = py.position()
        
        py.moveTo(s_x, sh)
        t.sleep(delay)
        
        k.press('1')
        py.rightClick()
        k.release('1')
        
        t.sleep(0.01)
        
        k.press('2')
        py.rightClick()
        k.release('2')
        
        py.moveTo(s_x, s_y)
        t.sleep(delay)

k.hook(jasnysad)

p(r"""
.-. .-.  .--.  .---.  .--.  .-. .-.  .--.  
| |/ /  / {} \{_   _}/ {} \ |  `| | / {} \ 
| |\ \ /  /\  \ | | /  /\  \| |\  |/  /\  \
`-' `-'`-'  `-' `-' `-'  `-'`-' `-'`-'  `-'   by @jasnysad for @4fth

                        bind: X
                        

""")
k.wait(wyjscie)
#       ^ bind off