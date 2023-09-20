import serial
import time

UART_DRIVER=serial.Serial('/dev/ttyS14', baudrate=115200)

def one_liter_forward():
    #period
    UART_DRIVER.write(str.encode('0'))
    time.sleep(0.01)
    UART_DRIVER.write(str.encode('0'))
    time.sleep(0.01)
    UART_DRIVER.write(str.encode('0'))
    time.sleep(0.01)
    UART_DRIVER.write(str.encode('1'))
    time.sleep(0.01)
    #direction
    UART_DRIVER.write(str.encode('0'))
    time.sleep(0.01)
    #nominator
    UART_DRIVER.write(str.encode('0'))
    time.sleep(0.01)
    UART_DRIVER.write(str.encode('0'))
    time.sleep(0.01)
    UART_DRIVER.write(str.encode('0'))
    time.sleep(0.01)
    UART_DRIVER.write(str.encode('1'))
    time.sleep(0.01)
    #denominator
    UART_DRIVER.write(str.encode('0'))
    time.sleep(0.01)
    UART_DRIVER.write(str.encode('0'))
    time.sleep(0.01)
    UART_DRIVER.write(str.encode('0'))
    time.sleep(0.01)
    UART_DRIVER.write(str.encode('1'))
    time.sleep(0.01)
    UART_DRIVER.write(str.encode('\r'))
    time.sleep(0.01)

def one_liter_backward():
    #period
    UART_DRIVER.write(str.encode('0'))
    time.sleep(0.01)
    UART_DRIVER.write(str.encode('0'))
    time.sleep(0.01)
    UART_DRIVER.write(str.encode('0'))
    time.sleep(0.01)
    UART_DRIVER.write(str.encode('1'))
    time.sleep(0.01)
    #direction
    UART_DRIVER.write(str.encode('1'))
    time.sleep(0.01)
    #nominator
    UART_DRIVER.write(str.encode('0'))
    time.sleep(0.01)
    UART_DRIVER.write(str.encode('0'))
    time.sleep(0.01)
    UART_DRIVER.write(str.encode('0'))
    time.sleep(0.01)
    UART_DRIVER.write(str.encode('1'))
    time.sleep(0.01)
    #denominator
    UART_DRIVER.write(str.encode('0'))
    time.sleep(0.01)
    UART_DRIVER.write(str.encode('0'))
    time.sleep(0.01)
    UART_DRIVER.write(str.encode('0'))
    time.sleep(0.01)
    UART_DRIVER.write(str.encode('1'))
    time.sleep(0.01)
    UART_DRIVER.write(str.encode('\r'))
    time.sleep(0.01)

def onetwelve_liter_forward():
    #period
    UART_DRIVER.write(str.encode('0'))
    time.sleep(0.01)
    UART_DRIVER.write(str.encode('0'))
    time.sleep(0.01)
    UART_DRIVER.write(str.encode('0'))
    time.sleep(0.01)
    UART_DRIVER.write(str.encode('1'))
    time.sleep(0.01)
    UART_DRIVER.write(str.encode(' '))
    time.sleep(0.01)
    #direction
    UART_DRIVER.write(str.encode('0'))
    time.sleep(0.01)
    UART_DRIVER.write(str.encode(' '))
    time.sleep(0.01)
    #nominator
    UART_DRIVER.write(str.encode('0'))
    time.sleep(0.01)
    UART_DRIVER.write(str.encode('0'))
    time.sleep(0.01)
    UART_DRIVER.write(str.encode('0'))
    time.sleep(0.01)
    UART_DRIVER.write(str.encode('1'))
    time.sleep(0.01)
    UART_DRIVER.write(str.encode(' '))
    time.sleep(0.01)
    #denominator
    UART_DRIVER.write(str.encode('0'))
    time.sleep(0.01)
    UART_DRIVER.write(str.encode('0'))
    time.sleep(0.01)
    UART_DRIVER.write(str.encode('1'))
    time.sleep(0.01)
    UART_DRIVER.write(str.encode('2'))
    time.sleep(0.01)
    UART_DRIVER.write(str.encode(' '))
    time.sleep(0.01)
    UART_DRIVER.write(str.encode('5'))
    time.sleep(0.01)
    UART_DRIVER.write(str.encode('0'))
    time.sleep(0.01)
    UART_DRIVER.write(str.encode('0'))
    time.sleep(0.01)
    UART_DRIVER.write(str.encode('0'))
    time.sleep(0.01)
    UART_DRIVER.write(str.encode(' '))
    time.sleep(0.01)
    UART_DRIVER.write(str.encode('\r'))
    time.sleep(0.01)

def onetwelve_liter_backward():
    #period
    UART_DRIVER.write(str.encode('0'))
    time.sleep(0.01)
    UART_DRIVER.write(str.encode('0'))
    time.sleep(0.01)
    UART_DRIVER.write(str.encode('0'))
    time.sleep(0.01)
    UART_DRIVER.write(str.encode('1'))
    time.sleep(0.01)
    UART_DRIVER.write(str.encode(' '))
    time.sleep(0.01)
    #direction
    UART_DRIVER.write(str.encode('1'))
    time.sleep(0.01)
    UART_DRIVER.write(str.encode(' '))
    time.sleep(0.01)
    #nominator
    UART_DRIVER.write(str.encode('0'))
    time.sleep(0.01)
    UART_DRIVER.write(str.encode('0'))
    time.sleep(0.01)
    UART_DRIVER.write(str.encode('0'))
    time.sleep(0.01)
    UART_DRIVER.write(str.encode('1'))
    time.sleep(0.01)
    UART_DRIVER.write(str.encode(' '))
    time.sleep(0.01)
    #denominator
    UART_DRIVER.write(str.encode('0'))
    time.sleep(0.01)
    UART_DRIVER.write(str.encode('0'))
    time.sleep(0.01)
    UART_DRIVER.write(str.encode('1'))
    time.sleep(0.01)
    UART_DRIVER.write(str.encode('2'))
    time.sleep(0.01)
    UART_DRIVER.write(str.encode(' '))
    time.sleep(0.01)
    #time
    UART_DRIVER.write(str.encode('5'))
    time.sleep(0.01)
    UART_DRIVER.write(str.encode('0'))
    time.sleep(0.01)
    UART_DRIVER.write(str.encode('0'))
    time.sleep(0.01)
    UART_DRIVER.write(str.encode('0'))
    time.sleep(0.01)
    UART_DRIVER.write(str.encode(' '))
    time.sleep(0.01)
    UART_DRIVER.write(str.encode('\r'))
    time.sleep(0.01)

class PARAMENTS:
    def __init__(self,period,dir,nom,denom,when_change):
        self.period=period
        self.dir=dir
        self.nom=nom
        self.denom=denom
        self.when_change=when_change
    def run(self):
        period=self.period
        dir=self.dir
        nom=self.nom
        denom=self.denom
        when_change=self.when_change
        spacebar=' '
        if(check_paramets(period,dir,nom,denom)==0):
            paraments=[period,dir,nom,denom,when_change,'\r']
            string_to_send=spacebar.join(paraments)
            print(string_to_send)
            UART_DRIVER.write(str.encode(string_to_send))
        else:
            print('Wprowadzono błędne argumenty')

def check_paramets(x,y,z,c):
    period=int(x)
    dir=int(y)
    nom=int(c)
    denom=int(z)
    if(period>9999 or denom>9999 or nom>999 or dir>2):
        return 1
    else:
        return 0

def get_data():
    period=input("Podaj okres impulsu (w ms): ")
    dir=input("Podaj kierunek kręcenia (0 - w przód, 1 - w tył): ")
    nom=input("Podaj licznik ułamka obrotu: ")
    denom=input("Podaj mianownik ułamka obrotu: ")
    when_change=input("Podaj okres, po którym silnik zacznie obracać się w przeciwnym kierunku (w ms): ")
    driver_paraments=PARAMENTS(period,dir,nom,denom,when_change)
    driver_paraments.run()

def onetwelve_liter_forward_new():
    string_to_send='100 0 1 12 5000 \r'
    UART_DRIVER.write(str.encode(string_to_send))  
    
def onetwelve_liter_backward_new():
    string_to_send='100 1 1 12 500 \r'
    UART_DRIVER.write(str.encode(string_to_send))
    UART_DRIVER.read()
def multiple_runs():
    string_to_send='1 0 1 1 0 \r'
    UART_DRIVER.write(str.encode(string_to_send))
    read_from_stm=int(UART_DRIVER.readline())
    if(read_from_stm==2):
        read_from_stm=0
        string_to_send='1 1 1 1 0 \r'
        UART_DRIVER.write(str.encode(string_to_send)) 
        read_from_stm=int(UART_DRIVER.readline())
        if(read_from_stm==2):
            string_to_send='1 0 1 1 99999999 \r'
            UART_DRIVER.write(str.encode(string_to_send))

def main():
    # get_data()
    # onetwelve_liter_forward_new()
    multiple_runs()
if __name__ == "__main__":
    main()