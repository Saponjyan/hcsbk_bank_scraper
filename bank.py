# from selenium.webdriver import Chrome
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




############################################################

def sti():
#     try:
        
#         baza=[]
#         value1 = login.get()
#         value2 = password.get()
#         global s1
#         s1 = int(sumot1.get())
#         global s2
#         s2 = int(sumdo1.get())
#         global k1
#         k1 = int(kefdo1.get())
#         sh = int(shag1.get())
#         global v1
#         v1 = int(vozot1.get())
#         global v2
#         v2 = int(vozdo1.get())
#         n1 = int(nakop1.get())
#         n2 = int(nakop2.get())
#         #text1.insert(0.0,f'{count} {sms} \n')
#         dat=[]
        
#         dat.append(value1)
#         dat.append(value2)
#         dat.append(s1)
#         dat.append(s2)
#         dat.append(k1)
#         dat.append(sh)
#         dat.append(v1)
#         dat.append(v2)
#         dat.append(n1)
#         dat.append(n2)
#         with open("log.csv","w") as f:
#             writer = csv.writer(f)
#             writer = writer.writerow(dat)
#         f.close()

#         global t
#         t=False
#         options = webdriver.ChromeOptions()
#         options.add_argument("--disable-blink-features=AutomationControlled")
# #############################################
#         head={'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
#         sec= requests.get('http://saponjyan.ru/arduinobank.html',headers=head)
#         sec2 = BeautifulSoup(sec.text,"lxml")
#         se=sec2.find("h1").text.split()
#         se=se[0]
#         #print(se[0])
#         if se == "404":
#             t=True
# ##################################
#     #options.headless = False

#         chrome_service = ChromeService('chromedriver')
#         chrome_service.creationflags = CREATE_NO_WINDOW
#         global driver2
#         driver2 = webdriver.Chrome(service=chrome_service)

#         #text1.delete(0.0,'end')
#     ######################################################################
#         # chrome_service = ChromeService('chromedriver')
#         # chrome_service.creationflags = CREATE_NO_WINDOW
#         # global driver2
#         # driver2 = webdriver.Chrome(service=chrome_service)


# #driver2 = Chrome('chromedriver')#,chrome_options=options
#         url1='https://online.hcsbk.kz/UserAccount/Login'

    
#         driver2.get(url1)
#         sleep(3)

#     ####################################################################

    
#         log = driver2.find_element(By.XPATH,'/html/body/div[8]/main/div/div/div/section/div[2]/div[1]/div[1]/form/div/input[1]')
#         pas = driver2.find_element(By.XPATH,'/html/body/div[8]/main/div/div/div/section/div[2]/div[1]/div[1]/form/div/input[2]')
#         log.send_keys(value1)##7476563190   7021314342
#         pas.send_keys(value2) #1700957kk #  Qwerty789!
#         but=driver2.find_element(By.XPATH,'/html/body/div[8]/main/div/div/div/section/div[2]/div[1]/div[1]/form/input[3]')

#         sleep(2)
#         but.click()
#         sleep(1)
#         poisk=driver2.find_element(By.XPATH,'/html/body/div[5]/div[5]/div[2]/ul/li[2]/a/span')
#         sleep(1)
#         poisk.click()
#         sleep(2)
#         klo=driver2.find_element(By.XPATH,'/html/body/div[5]/div[9]/div/div[1]/div/div[1]/form/div[4]/div/div/input[2]')
#         sleep(1)
#         klo.click()
#         sleep(2)                          
#         iskat=driver2.find_element(By.XPATH,'/html/body/div[5]/div[9]/div/div[1]/div/div[1]/form/div[5]/div[3]/div/div/button')
#         sleep(2)
#         iskat.click()
#         sleep(3)                           
#         mil=driver2.find_element(By.XPATH,'/html/body/div[5]/div[5]/div[9]/div/div[1]/div/div[1]/form/div[5]/div[2]/div/div/input')
#         sleep(2)
#         mil.send_keys(Keys.CONTROL+"a")
#         sleep(1)
#         mil.send_keys(Keys.DELETE)
#         sleep(1)
#         mil.send_keys(f'{v2}')
#         sleep(1)
#         mil2=driver2.find_element(By.XPATH,'/html/body/div[5]/div[5]/div[9]/div/div[1]/div/div[1]/form/div[5]/div[1]/div/div/input')
#         sleep(1)
#         mil2.send_keys(Keys.CONTROL+"a")
#         mil2.send_keys(Keys.DELETE)
#         mil2.send_keys(f'{v1}')
#         sleep(1)                              
#         iskdep=driver2.find_element(By.XPATH,'/html/body/div[5]/div[5]/div[9]/div/div[1]/div/div[1]/form/div[5]/div[3]/div/div/button')
#         sleep(1)
#         iskdep.click()
#         stug()
#     except:
#         print('a')
#         #driver2.quit()
#         stug()
    baza=[]
    value1 = login.get()
    value2 = password.get()
    global s1
    s1 = int(sumot1.get())
    global s2
    s2 = int(sumdo1.get())
    global k1
    k1 = int(kefdo1.get())
    sh = int(shag1.get())
    global v1
    v1 = int(vozot1.get())
    global v2
    v2 = int(vozdo1.get())
    n1 = int(nakop1.get())
    n2 = int(nakop2.get())
    #text1.insert(0.0,f'{count} {sms} \n')
    dat=[]
        
    dat.append(value1)
    dat.append(value2)
    dat.append(s1)
    dat.append(s2)
    dat.append(k1)
    dat.append(sh)
    dat.append(v1)
    dat.append(v2)
    dat.append(n1)
    dat.append(n2)
    with open("log.csv","w") as f:
        writer = csv.writer(f)
        writer = writer.writerow(dat)
    f.close()

    global t
    t=False
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
#############################################
    # head={'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
    # sec= requests.get('http://saponjyan.ru/arduinobank.html',headers=head)
    # sec2 = BeautifulSoup(sec.text,"lxml")
    # se=sec2.find("h1").text.split()
    # se=se[0]
    #     #print(se[0])
    # if se == "404":
    #     t=True
##################################
    #options.headless = False

    chrome_service = ChromeService('chromedriver')
    chrome_service.creationflags = CREATE_NO_WINDOW
    global driver2
    driver2 = webdriver.Chrome(service=chrome_service)

        #text1.delete(0.0,'end')
    ######################################################################
        # chrome_service = ChromeService('chromedriver')
        # chrome_service.creationflags = CREATE_NO_WINDOW
        # global driver2
        # driver2 = webdriver.Chrome(service=chrome_service)


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
    sleep(2)
    poisk=driver2.find_element(By.XPATH,'/html/body/div[5]/div[5]/div[2]/ul/li[2]/a/span')
    sleep(2)
    poisk.click()
    sleep(3)
    klo=driver2.find_element(By.XPATH,'/html/body/div[5]/div[9]/div/div[1]/div/div[1]/form/div[4]/div/div/input[2]')
    sleep(3)
    klo.click()
    sleep(2)                          
    iskat=driver2.find_element(By.XPATH,'/html/body/div[5]/div[9]/div/div[1]/div/div[1]/form/div[5]/div[3]/div/div/button')
    sleep(2)
    iskat.click()
    sleep(8)                           
    mil=driver2.find_element(By.XPATH,'/html/body/div[5]/div[5]/div[9]/div/div[1]/div/div[1]/form/div[5]/div[2]/div/div/input')
    sleep(2)
    mil.send_keys(Keys.CONTROL+"a")
    sleep(1)
    mil.send_keys(Keys.DELETE)
    sleep(1)
    mil.send_keys(f'{v2}')
    sleep(1)
    mil2=driver2.find_element(By.XPATH,'/html/body/div[5]/div[5]/div[9]/div/div[1]/div/div[1]/form/div[5]/div[1]/div/div/input')
    sleep(1)
    mil2.send_keys(Keys.CONTROL+"a")
    mil2.send_keys(Keys.DELETE)
    mil2.send_keys(f'{v1}')
    sleep(1)                              
    iskdep=driver2.find_element(By.XPATH,'/html/body/div[5]/div[5]/div[9]/div/div[1]/div/div[1]/form/div[5]/div[3]/div/div/button')
    sleep(1)
    iskdep.click()
    stug()
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
            # baza.append(f"Сумма {sumv}\nВознаграждения {voz}\nИтог {itog}\n кэф {kaf}")
            # with open("baza.csv", "a", encoding='utf8', newline='') as f2:
            #     baz=csv.writer(f2,delimiter=",")
            #     baz=baz.writerow(baza)
            # baza=[]
            #print(kaf)
        except:
        #kaf=int(int(sumv)/int(voz))
            print("int eror")
        if kaf<=k1 and s1<int(itog)<s2:#and v1<voz<v2:
            print(kaf,k1)
            sleep(2)                                    #/html/body/div[5]/div[5]/div[9]/div/div[1]/div/div[3]/div[2]/div[2]/div/div[1]/div/div[8]/button/text()
            kupit=driver2.find_element(By.XPATH,f'/html/body/div[5]/div[5]/div[9]/div/div[1]/div/div[{z}]/div[2]/div[2]/div/div[1]/div/div[8]/button')
            sleep(1)                              
            kupit.click()
            #telegram_send.send(messages=[f"Поиск по Вознаграждению\nСумма {sumv}\nВознаграждения {voz}\nИтоговая Сумма {itog}\n коэффициент {kaf}"])
            
            #print('ПОКУПАЮ!!!!!!!!!!!!!!')
            text1.insert(0.0,[f"ПОКУПАЮ!!!!!!!!!!!!!!\nСумма {sumv}\nВознаграждения {voz}\nИтог {itog}\n кэф {kaf}"])
            sleep(600)
        else:
            #print('неподходит')
            text1.insert(0.0,[f"не смог Сумма {sumv}\nВознаграждения {voz}\nИтог {itog}\n кэф {kaf}"])
            sleep(2)
            #telegram_send.send(messages=[f'не подходит!!!\n Итоговая Сумма {sumv}\n возногрождения {voz} \n kef{kaf}'])
            
            
        #print(z)




#######################################
def stug():

    count=0
    #t=True
    while t:
        
        

    

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
            #sti()


    
###############################################################
        # if __name__ == '__main__':
#     main()
win = tk.Tk()
win.title('Saponjyan.ru')
win.geometry("400x600")
win.resizable(False,False)
win.iconbitmap('bab.ico')
# chek1=tk.Checkbutton(win,text='Start Scraping',command=stug,indicatoron=False)
# chek1.pack()
global tex
text1=tk.Text(win,width=85,height=10)

log_text=tk.Label(win,text='Логин')
pass_text=tk.Label(win,text='Пароль')

text1.pack()
log_text.pack()

login=tk.Entry(win)
login.insert(0,r[0])
password=tk.Entry(win)
password.insert(0,r[1])


login.pack()
pass_text.pack()
password.pack()
sumot=tk.Label(win,text='Стоимость жиля от')
sumot.pack()
sumot1=tk.Entry(win)
sumot1.pack()
sumot1.insert(0,r[2])
sumdo=tk.Label(win,text='Стоимость жиля  до')
sumdo.pack()

sumdo1=tk.Entry(win)
sumdo1.pack()
sumdo1.insert(0,r[3])
shag=tk.Label(win,text='шаг')
shag.pack()

shag1=tk.Entry(win)
shag1.pack()
shag1.insert(0,r[5])
kefdo=tk.Label(win,text='коэффициент до')
kefdo.pack()
kefdo1=tk.Entry(win)
kefdo1.pack()
kefdo1.insert(0,r[4])

vozot=tk.Label(win,text='вознаграждение от')
vozot.pack()
vozot1=tk.Entry(win)
vozot1.pack()
vozot1.insert(0,r[6])
vozdo=tk.Label(win,text='вознаграждение до')
vozdo.pack()
vozdo1=tk.Entry(win)
vozdo1.pack()
vozdo1.insert(0,r[7])
nakop=tk.Label(win,text='Сумма вклада от')
nakop.pack()
nakop1=tk.Entry(win)
nakop1.pack()
nakop1.insert(0,r[8])
nako=tk.Label(win,text='Сумма вклада до')
nako.pack()
nakop2=tk.Entry(win)
nakop2.pack()
nakop2.insert(0,r[9])
btn= tk.Button(win,text='Start',command=st)
btn.pack()
#btn2= tk.Button(win,text='Start2',command=st).pack()

win.mainloop() 