from math import *

CSI = f'\x1B['

RESET = f'{CSI}0m'
ERASE = f'{CSI}2K'
START = f'{CSI}0G'
probel = '  '

def flag():
    size = int(input('Введите размер флага (вертикальный): '))//2*2 +1
    r = ceil(size/4)
    field = [[x,y] for y in range(size) for x in range(int(size*1.8))]
    center = [(int(size*1.8)-1)//2, (size - 1)//2]
    karta = f''
    last = 0
    for point in field:
        x,y = point
        if y == last:
            if dist(point, center) <r:
                karta+='к'
            else:
                karta+='б'
        else:
            karta+='\nб'
        last = y
    karta = karta.replace('б', f'{CSI}48;5;15m{probel}{RESET}')
    karta = karta.replace('к', f'{CSI}48;5;196m{probel}{RESET}')
    print(karta)
flag()

# print(f'{RESET}ntncn')
# print(f'{CSI}48;5;118m{CSI}38;5;18m   {RESET}')
# print(f'{CSI}48;5;118m{CSI}38;5;18m   {RESET}')