from math import *
f = open('sequence.txt')
A = [float(i) for i in f]
f.close()
CSI = f'\x1B['

print(A[:10])
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

def uzor(repeat):
    uzor =f'{"DDDSDDDDDSDD"*repeat}D\n\
{"DDSDSDDDSDSD"*repeat}D\n\
{"DSDDDSDSDDDS"*repeat}D\n\
{"SDDDDDSDDDDD"*repeat}S\n\
{"DSDDDSDSDDDS"*repeat}D\n\
{"DDSDSDDDSDSD"*repeat}D\n\
{"DDDSDDDDDSDD"*repeat}D'
    uzor = uzor.replace('D',f'{CSI}48;5;118m{probel}{RESET}')
    uzor = uzor.replace('S',f'{CSI}48;5;160m{probel}{RESET}')
    print(uzor)

def diagramma(spis):
    otr = [i for i in spis if i<=0]
    vsego = len(otr)
    bol5 = [i for i in otr if i>-5] 
    men5 = [i for i in otr if i<-5]
    dolya_bol = int((len(bol5)/vsego)*100)
    print(f'Больше -5:{CSI}48;5;118m{" "*dolya_bol}{CSI}11G{CSI}38;5;196m{str(dolya_bol)+'%'}{RESET}')
    print(f'Меньше -5:{CSI}48;5;118m{" "*(100-dolya_bol)}{CSI}11G{CSI}38;5;196m{str(100-dolya_bol)+'%'}{RESET}')
        
diagramma(A)
# print(f'{RESET}ntncn')
# print(f'{CSI}48;5;118m{CSI}38;5;18m   {RESET}')
# print(f'{CSI}48;5;118m{CSI}38;5;18m   {RESET}')