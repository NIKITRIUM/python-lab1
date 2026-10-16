from math import dist, ceil
import os
from time import sleep

from animation_frames import frame1, frame2, frame3, frame4, frame5

f = open('sequence.txt')
data = [float(i) for i in f]
f.close()

CSI = f'\x1B['

RESET = f'{CSI}0m'
ERASE = f'{CSI}2K'
START = f'{CSI}0G'
gap= '  '

def flag():
    size = int(input('Введите размер флага (вертикальный): '))//2*2 +1
    r = ceil(size/4)
    field = [[x,y] for y in range(size) for x in range(int(size*1.8))]
    center = [(int(size*1.8)-1)//2, (size - 1)//2]
    flag_map = f''
    last = 0
    for point in field:
        x,y = point
        if y == last:
            if dist(point, center) <r:
                flag_map += 'к'
            else:
                flag_map += 'б'
        else:
            flag_map += '\nб'
        last = y
    flag_map = flag_map.replace('б', f'{CSI}48;5;15m{gap}{RESET}')
    flag_map = flag_map.replace('к', f'{CSI}48;5;196m{gap}{RESET}')
    print(flag_map)

def pattern(repeat, width):
    pattern =f'{"DDDSDDDDDSDD"*repeat}D\n\
{"DDSDSDDDSDSD"*repeat}D\n\
{"DSDDDSDSDDDS"*repeat}D\n\
{"SDDDDDSDDDDD"*repeat}S\n\
{"DSDDDSDSDDDS"*repeat}D\n\
{"DDSDSDDDSDSD"*repeat}D\n\
{"DDDSDDDDDSDD"*repeat}D'
    pattern = pattern.replace('D',f'{CSI}48;5;118m{" "*width}{RESET}')
    pattern = pattern.replace('S',f'{CSI}48;5;160m{" "*width}{RESET}')
    print(pattern)

def diagram(data_list):
    negative_numbers = [i for i in data_list if i<=0]
    all_num = len(negative_numbers)
    above_minus_5 = [i for i in negative_numbers if i>-5] 
    part_above = int((len(above_minus_5)/all_num)*100)
    print(f'Больше -5:{CSI}48;5;118m{" "*part_above}{CSI}11G{CSI}38;5;196m{str(part_above)+'%'}{RESET}')
    print(f'Меньше -5:{CSI}48;5;118m{" "*(100-part_above)}{CSI}11G{CSI}38;5;196m{str(100-part_above)+'%'}{RESET}')

def animation():
    os.system("cls")
    frame1()
    sleep(1.5)
    os.system("cls")
    frame2()
    sleep(1.5)
    os.system("cls")
    frame3()
    sleep(1.5)    
    os.system("cls")
    frame4()
    sleep(1.5)  
    os.system("cls")
    frame5()


def func():
    os.system("cls")
    print('y')
    for i in range(20,0,-1):
        print(f' {i}'[-2:])
        print('  ')
    print(' 0 1 2 3 4 5 6 7 8 9 x', end='')
    print(f'{CSI}2G', end='')
    y = 0
    for x in range(0,15):
        while y<3*x:
            print(f'{CSI}1A{CSI}48;5;15m {CSI}1D', end='')
            y+=1
        print(f'{CSI}1C', end='')
    
    print(f'{RESET}')
    print(f'{CSI}900B')


diagram(data)

# ПОПРАВИТЬ:
# 1) ТРАНСЛИТ
# 2) НАЗВАНИЯ ПЕРЕМЕННЫХ
# 3) УЗОР ФУНКЦИЮ
# 4) ОТСТУПЫ В ПЕРЕМЕННЫХ