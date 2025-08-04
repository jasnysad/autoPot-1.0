from pynput.mouse import Controller, Button
import keyboard as k
import time as t

mouse = Controller()

p = print

wlacz = 'x'         # Aktywacja                | bind x
wyjscie = '='       # De-aktywacja             | bind =
delay = 0.05        # Delay przed zmiana slotu 
cooldown = 0.5      # Minimalny odstęp czasowy między kolejnymi aktywacjami funkcji ruch/klik
ltt = 0             # Timestamp ostatniego wywołania funkcji, potrzebny do sprawdzenia cooldown


def ruch(dy, steps=15, delay_per_step=0.005):
    dy_per_step = dy / steps
    for _ in range(steps):
        mouse.move(0, dy_per_step)
        t.sleep(delay_per_step)

def jasnysad(event):
    global ltt
    if event.name == wlacz and event.event_type == 'down':
        if t.time() - ltt < cooldown:
            return
        ltt = t.time()

        ruch(900)

        k.send('6')
        mouse.click(Button.right)

        t.sleep(delay)

        k.send('r')
        mouse.click(Button.right)

        ruch(-900)

k.hook(jasnysad)

p(r"""
.-. .-.  .--.  .---.  .--.  .-. .-.  .--.  
| |/ /  / {} \{_   _}/ {} \ |  `| | / {} \ 
| |\ \ /  /\  \ | | /  /\  \| |\  |/  /\  \
`-' `-'`-'  `-' `-' `-'  `-'`-' `-'`-'  `-'   by @jasnysad for @4fth

                        bind: X
""")
k.wait(wyjscie)


