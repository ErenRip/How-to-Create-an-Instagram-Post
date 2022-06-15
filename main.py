from cmath import e
import click
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os
from users import kullanıcıadı, sifre
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from colorama import Fore, Back, Style, init
init(autoreset=True)

#Post settings or CFG
print(f'{Fore.YELLOW}{Back.BLACK}[+]{Fore.WHITE}Instagram Fotoğraf Yükleme Aracı v1.0')
print(' ')
print(' ')
acıklama= input(f'''{Fore.RED}lütfen gönderinin altına yazılıcak 
açıklamayı giriniz Sınır 2000 karakter:{Fore.WHITE} ''')
print(' ')
print(' ')
etiket= input(f'''Lütfen gönderinin için herhangibi # etiketi varsa 
giriniz örnek giriş ( #keşfet #deneme #beğeni ) gibi giriniz ne kadar etiket varsa: ''')
#Web
driver = webdriver.Chrome()
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(2)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(kullanıcıadı)
time.sleep(1)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(sifre)
time.sleep(1)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').send_keys(Keys.ENTER)


os.system('cls')
endtext=(f'''{acıklama}


{etiket}
''')
print('45 saniye Başladı')
i=0
while True:
    i=i+1
    print(i)
    time.sleep(1)
    if(i==45):
        print('45 saniye bitti')
        break
driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/div/div/div[2]/div[1]/div/div/div/div[1]/div/div[2]/div/button').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/div/div/div[2]/div[1]/div/div/div/div[1]/div/div[1]/div/button[1]').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/div/div/div[1]/div/div/div[3]/div/button').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/div/div/div[1]/div/div/div[3]/div/button').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/textarea').send_keys(endtext)
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/div/div/div[1]/div/div/div[3]/div/button').click()
time.sleep(5)
driver.close()
os.system('cls')
print(f'{Fore.YELLOW}[+]{Fore.WHITE}Yükleme Başarılı')

