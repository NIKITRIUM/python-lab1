CSI = f'\x1B['

RESET = f'{CSI}0m'
ERASE = f'{CSI}2K'
START = f'{CSI}0G'

def frame1():
    print(' ')
    print(f'{CSI}4G{CSI}48;5;217m{CSI}38;5;13m(xx){RESET}')
    print(f'{CSI}2G{CSI}48;5;217m{CSI}38;5;13m<-    ->{RESET}')
    print(f'{CSI}2G{CSI}48;5;217m{CSI}38;5;13m|{RESET} {CSI}48;5;217m    {RESET} {CSI}48;5;217m|{RESET}')
    print(f'{CSI}2G{CSI}48;5;217m{CSI}38;5;13m^{RESET} {CSI}48;5;217m <> {RESET} {CSI}48;5;217m^{RESET}')
    print(f'{CSI}3G{CSI}48;5;217m{CSI}38;5;13m/ {RESET}  {CSI}48;5;217m \\{RESET}')
    print(f'{CSI}3G{CSI}48;5;217m{CSI}38;5;13m| {RESET}  {CSI}48;5;217m |{RESET}')
    print(f'{CSI}3G{CSI}48;5;217m{CSI}38;5;13mI {RESET}  {CSI}48;5;217m I{RESET}')    

def frame2():
    print(' ')
    print(f'{CSI}4G{CSI}48;5;217m{CSI}38;5;13m(00){RESET}')
    print(f'{CSI}2G{CSI}48;5;217m{CSI}38;5;13m<-    ->{RESET}')
    print(f'{CSI}2G{CSI}48;5;217m{CSI}38;5;13m|{RESET} {CSI}48;5;217m    {RESET} {CSI}48;5;217m|{RESET}')
    print(f'{CSI}2G{CSI}48;5;77m{CSI}38;5;82mм{RESET} {CSI}48;5;217m <> {RESET} {CSI}38;5;82m{CSI}48;5;77mм{RESET}')
    print(f'{CSI}3G{CSI}48;5;217m{CSI}38;5;13m/ {RESET}  {CSI}48;5;217m \\{RESET}')
    print(f'{CSI}3G{CSI}48;5;217m{CSI}38;5;13m| {RESET}  {CSI}48;5;217m |{RESET}')
    print(f'{CSI}3G{CSI}48;5;77m{CSI}38;5;82mЯ {RESET}  {CSI}48;5;77m R{RESET}') 

def frame3():
    print(' ')
    print(f'{CSI}4G{CSI}48;5;217m{CSI}38;5;13m(00){RESET}')
    print(f'{CSI}2G{CSI}48;5;217m{CSI}38;5;13m<-    ->{RESET}')
    print(f'{CSI}2G{CSI}48;5;217m{CSI}38;5;13m|{RESET} {CSI}48;5;217m    {RESET} {CSI}48;5;217m|{RESET}')
    print(f'{CSI}2G{CSI}48;5;77m{CSI}38;5;82mм{RESET} {CSI}48;5;217m <> {RESET} {CSI}38;5;82m{CSI}48;5;77mм{RESET}')
    print(f'{CSI}3G{CSI}48;5;8m{CSI}38;5;7m/ {RESET}  {CSI}48;5;8m{CSI}38;5;7m \\{RESET}')
    print(f'{CSI}3G{CSI}48;5;8m{CSI}38;5;7m| {RESET}  {CSI}48;5;8m{CSI}38;5;7m |{RESET}')
    print(f'{CSI}3G{CSI}48;5;77m{CSI}38;5;82mЯ {RESET}  {CSI}48;5;77m R{RESET}')

def frame4():
    print(' ')
    print(f'{CSI}4G{CSI}48;5;217m{CSI}38;5;13m(++){RESET}')
    print(f'{CSI}2G{CSI}48;5;196m{CSI}38;5;210m<-    ->{RESET}')
    print(f'{CSI}2G{CSI}48;5;196m{CSI}38;5;210m|{RESET} {CSI}48;5;196m{CSI}38;5;210m LV {RESET} {CSI}38;5;210m{CSI}48;5;196m|{RESET}')
    print(f'{CSI}2G{CSI}48;5;77m{CSI}38;5;82mм{RESET} {CSI}48;5;196m    {RESET} {CSI}38;5;82m{CSI}48;5;77mм{RESET}')
    print(f'{CSI}3G{CSI}48;5;8m{CSI}38;5;7m/ {RESET}  {CSI}48;5;8m{CSI}38;5;7m \\{RESET}')
    print(f'{CSI}3G{CSI}48;5;8m{CSI}38;5;7m| {RESET}  {CSI}48;5;8m{CSI}38;5;7m |{RESET}')
    print(f'{CSI}3G{CSI}48;5;77m{CSI}38;5;82mЯ {RESET}  {CSI}48;5;77m R{RESET}')

def frame5():
    print(f'{CSI}5G{CSI}48;5;70m{CSI}38;5;82m<>{RESET}')
    print(f'{CSI}4G{CSI}48;5;70m{CSI}38;5;82m{{**}}{RESET}')
    print(f'{CSI}2G{CSI}48;5;196m{CSI}38;5;210m<-    ->{RESET}')
    print(f'{CSI}2G{CSI}48;5;196m{CSI}38;5;210m|{RESET} {CSI}48;5;196m{CSI}38;5;210m LV {RESET} {CSI}38;5;210m{CSI}48;5;196m|{RESET}')
    print(f'{CSI}2G{CSI}48;5;77m{CSI}38;5;82mм{RESET} {CSI}48;5;196m    {RESET} {CSI}38;5;82m{CSI}48;5;77mм{RESET}')
    print(f'{CSI}3G{CSI}48;5;8m{CSI}38;5;7m/ {RESET}  {CSI}48;5;8m{CSI}38;5;7m \\{RESET}')
    print(f'{CSI}3G{CSI}48;5;8m{CSI}38;5;7m| {RESET}  {CSI}48;5;8m{CSI}38;5;7m |{RESET}')      
    print(f'{CSI}3G{CSI}48;5;77m{CSI}38;5;82mЯ {RESET}  {CSI}48;5;77m R{RESET}')