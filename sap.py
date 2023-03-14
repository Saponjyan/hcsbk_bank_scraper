from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from subprocess import CREATE_NO_WINDOW
from selenium import webdriver
from time import sleep
#import telegram_send
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup

from threading import *
import tkinter as tk
import csv


############################################################
# def main():
with open("log.csv")as f:
    r=csv.reader(f)
    r=list(r)[0]

# t=False
############################################################

def sti():
    try:
        value1 = login.get()
        value2 = password.get()
        s1 = int(sumot1.get())
        s2 = int(sumdo1.get())
        k1 = int(kefdo1.get())
        #text1.delete(0.0,'end')
    ######################################################################
        chrome_service = ChromeService('chromedriver')
        chrome_service.creationflags = CREATE_NO_WINDOW

        driver2 = webdriver.Chrome(service=chrome_service)


#driver2 = Chrome('chromedriver')#,chrome_options=options
        url1='https://online.hcsbk.kz/UserAccount/Login'

    
        driver2.get(url1)
        sleep(3)

    ####################################################################

    
        log = driver2.find_element(By.XPATH,'/html/body/div[8]/main/div/div/div/section/div[2]/div[1]/div[1]/form/div/input[1]')
        pas = driver2.find_element(By.XPATH,'/html/body/div[8]/main/div/div/div/section/div[2]/div[1]/div[1]/form/div/input[2]')
        log.send_keys(value1)
        pas.send_keys(value2)
        but=driver2.find_element(By.XPATH,'/html/body/div[8]/main/div/div/div/section/div[2]/div[1]/div[1]/form/input[3]')

        sleep(2)
        but.click()
        poisk=driver2.find_element(By.XPATH,'/html/body/div[5]/div[5]/div[2]/ul/li[2]/a/span')
        sleep(1)
        poisk.click()
        klo=driver2.find_element(By.XPATH,'/html/body/div[5]/div[9]/div/div[1]/div/div[1]/form/div[4]/div/div/input[2]')
        klo.click()                          
        iskat=driver2.find_element(By.XPATH,'/html/body/div[5]/div[9]/div/div[1]/div/div[1]/form/div[5]/div[3]/div/div/button')
        sleep(3)
        iskat.click()
        sleep(3)
        mil=driver2.find_element(By.XPATH,'/html/body/div[5]/div[5]/div[9]/div/div[1]/div/div[1]/form/div[5]/div[2]/div/div/input')
        mil.send_keys(Keys.CONTROL+"a")
        mil.send_keys(Keys.DELETE)

        mil.send_keys('1000000')
        sleep(1)
        iskdep=driver2.find_element(By.XPATH,'/html/body/div[5]/div[5]/div[9]/div/div[1]/div/div[1]/form/div[5]/div[3]/div/div/button')
        sleep(2)
        iskdep.click()
        stug()
    except:
        print(a)
        # sti()
#######################################################################################
t1= Thread(target=sti)
#t2= Thread(target=sti)
def st():
    t1.start()
# def st2():    
#     t2.start()

def start():
    for z in range(3,10):

        itog=driver2.find_element(By.XPATH,f'/html/body/div[5]/div[5]/div[9]/div/div[1]/div/div[{z}]/div[2]/div[2]/div/div[1]/div/div[7]').text
        itog=itog[:-5]
        itog=itog.split()
        itog=''.join(itog)
        itog=int(itog)
        #print(itog)
###############################              /html/body/div[5]/div[5]/div[9]/div/div[1]/div/div[3]/div[2]/div[2]/div/div[1]/div/div[1]/div[2]/span[1]/text()
        sumv=driver2.find_element(By.XPATH,f'/html/body/div[5]/div[5]/div[9]/div/div[1]/div/div[{z}]/div[2]/div[2]/div/div[1]/div/div[1]/div[2]/span[1]').text
        sumv=sumv[:-3]
        sumv=sumv.split()
        sumv=''.join(sumv)
        
        #print(sumv)
###############################          
        voz=driver2.find_element(By.XPATH,f'/html/body/div[5]/div[5]/div[9]/div/div[1]/div/div[{z}]/div[2]/div[2]/div/div[1]/div/div[2]/div[2]').text
        voz=voz[:-4]
        voz=voz.split()
        voz=''.join(voz)
        kaf=5000
        #print(voz)
        
###############################
        try:
            kaf=int(int(sumv)/int(voz))
            #print(kaf)
        except:
            print("int eror")
        if kaf<=311:
                                                 #/html/body/div[5]/div[5]/div[9]/div/div[1]/div/div[3]/div[2]/div[2]/div/div[1]/div/div[8]/button/text()
            kupit=driver2.find_element(By.XPATH,f'/html/body/div[5]/div[5]/div[9]/div/div[1]/div/div[{z}]/div[2]/div[2]/div/div[1]/div/div[8]/button')
            kupit.click()
            #telegram_send.send(messages=[f"Поиск по Вознаграждению\nСумма {sumv}\nВознаграждения {voz}\nИтоговая Сумма {itog}\n коэффициент {kaf}"])
            sleep(2) 
            #print('ПОКУПАЮ!!!!!!!!!!!!!!')
            text1.insert(0.0,[f"ПОКУПАЮ!!!!!!!!!!!!!!\nСумма {sumv}\nВознаграждения {voz}\nИтог {itog}\n коэф {kaf}"])
            sleep(600)
        else:
            #print('неподходит')
            text1.insert(0.0,[f"не смог Сумма {sumv}\nВознаграждения {voz}\nИтог {itog}\n коэф {kaf}"])
            #telegram_send.send(messages=[f'не подходит!!!\n Итоговая Сумма {sumv}\n возногрождения {voz} \n kef{kaf}'])
            
            
        print(z)




#######################################
def stug():

    count=0
    t=True
    while t:
        sleep(1)
        

    

        try:
            isk=driver2.find_element(By.XPATH,'/html/body/div[5]/div[5]/div[9]/div/div[1]/div/div[1]/form/div[5]/div[3]/div/div/button')
            isk.click()
            sleep(2)
        except:
            count+=1
        #print('ne uspel')
        try:
            #text1.insert(0.0,f"{count} Ничего Нет\n")
            count+=1
            start()
        
        except:
            
            text1.insert(0.0,f"{count} Ничего Нет\n")
            #print('ошибка')


    
###############################################################
        # if __name__ == '__main__':
#     main()
win = tk.Tk()
win.title('Saponjyan.ru')
win.geometry("250x350")
win.resizable(False,False)
win.iconbitmap('bab.ico')
# chek1=tk.Checkbutton(win,text='Start Scraping',command=stug,indicatoron=False)
# chek1.pack()
global tex
text1=tk.Text(win,width=30,height=4)
loginl=tk.Label(win,text='Логин')
passwordl=tk.Label(win,text='Пароль')

login=tk.Entry(win)
password=tk.Entry(win)
text1.pack()
loginl.pack()
login.pack()
login.insert(0,r[0])
passwordl.pack()
password.pack()
password.insert(0,r[1])

sumot=tk.Label(win,text='Минимальное вознаграждение')
sumot.pack()
sumot1=tk.Entry(win)
sumot1.pack()
sumot1.insert(0,r[2])
sumdo=tk.Label(win,text='Максимальное вознаграждение')
sumdo.pack()

sumdo1=tk.Entry(win)
sumdo1.pack()
sumdo1.insert(0,r[3])

kefdo=tk.Label(win,text='коэффициент до')
kefdo.pack()
kefdo1=tk.Entry(win)
kefdo1.pack()
kefdo1.insert(0,r[4])


btn= tk.Button(win,text='Start',command=st).pack()
#btn2= tk.Button(win,text='Start2',command=st2).pack()

win.mainloop() 