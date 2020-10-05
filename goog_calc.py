"""
Tremebunda google calculator

By victorbacon
"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait


class DumbassBot():
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        
        
    def gocalc(self):
        self.driver.get("https://www.google.es/")
        
        #Cookies pop-up
        #self.driver.implicitly_wait(5)     PREVIOUS ATTEMPT TO SOLVE THE ISSUE
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('//*[@id="cnsw"]/iframe'))
        cooki = self.driver.find_element_by_xpath('//*[@id="introAgreeButton"]/span')
        cooki.click()
        self.driver.switch_to.default_content()
        
        #write calculator in the search bar
        barra = self.driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
        barra.send_keys('calculator')
        
        # The recent search tab opens and wont let us click on 'search'
        self.driver.switch_to_default_content()
                #anywhere = self.driver.find_element_by_xpath('//*[@id="hplogo"]')    PREVIOUS ATTEMPT TO SOLVE THE ISSUE
                #anywhere.click()
        
        #click search 
        busc_btn = self.driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]')
        busc_btn.click()
        
    def defnum(self):
        numlist=[]          #ordered from 0 to 9  [0,1,2,3,...9]
        numlist.append(self.driver.find_element_by_xpath('//*[@id="cwmcwd"]/div/div/div[3]/div/table[2]/tbody/tr[5]/td[1]/div/div'))
        numlist.append(self.driver.find_element_by_xpath('//*[@id="cwmcwd"]/div/div/div[3]/div/table[2]/tbody/tr[4]/td[1]/div/div'))
        numlist.append(self.driver.find_element_by_xpath('//*[@id="cwmcwd"]/div/div/div[3]/div/table[2]/tbody/tr[4]/td[2]/div/div'))
        numlist.append(self.driver.find_element_by_xpath('//*[@id="cwmcwd"]/div/div/div[3]/div/table[2]/tbody/tr[4]/td[3]/div/div'))
        numlist.append(self.driver.find_element_by_xpath('//*[@id="cwmcwd"]/div/div/div[3]/div/table[2]/tbody/tr[3]/td[1]/div/div'))
        numlist.append(self.driver.find_element_by_xpath('//*[@id="cwmcwd"]/div/div/div[3]/div/table[2]/tbody/tr[3]/td[2]/div/div'))
        numlist.append(self.driver.find_element_by_xpath('//*[@id="cwmcwd"]/div/div/div[3]/div/table[2]/tbody/tr[3]/td[3]/div/div'))
        numlist.append(self.driver.find_element_by_xpath('//*[@id="cwmcwd"]/div/div/div[3]/div/table[2]/tbody/tr[2]/td[1]/div/div'))
        numlist.append(self.driver.find_element_by_xpath('//*[@id="cwmcwd"]/div/div/div[3]/div/table[2]/tbody/tr[2]/td[2]/div/div'))
        numlist.append(self.driver.find_element_by_xpath('//*[@id="cwmcwd"]/div/div/div[3]/div/table[2]/tbody/tr[2]/td[3]/div/div'))
        return numlist
        
    def defop(self)  :      #ordered as [=,+,-]
        oplist=[]
        oplist.append(self.driver.find_element_by_xpath('//*[@id="cwmcwd"]/div/div/div[3]/div/table[2]/tbody/tr[5]/td[3]/div/div'))
        oplist.append(self.driver.find_element_by_xpath('//*[@id="cwmcwd"]/div/div/div[3]/div/table[2]/tbody/tr[5]/td[4]/div/div'))
        oplist.append(self.driver.find_element_by_xpath('//*[@id="cwmcwd"]/div/div/div[3]/div/table[2]/tbody/tr[4]/td[4]/div/div'))
        return oplist
        
        
        
        #Do the sum here bc Im not used to global and local variables
        #num4.click()
        #num0.click()
        #num4.click()
        #num1.click()
        #num9.click()
        
        #plus.click()
        
        #num1.click()
        #num7.click()
        #num5.click()
        #num8.click()
        #num9.click()
        
        #equal.click()
        
        
    def traduct(self, oper):         #input your operation as strings2+3
        numlist= self.defnum()
        oplist= self.defop()
        equal= oplist[0]
        for letr in oper:
            if letr=='0' :
                num= numlist[0]
            elif letr=='1' :
                num= numlist[1]
            elif letr=='2' :
                num= numlist[2]
            elif letr=='3' :
                num= numlist[3]
            elif letr=='4' :
                num= numlist[4]
            elif letr=='5' :
                num= numlist[5]
            elif letr=='6' :
                num= numlist[6]
            elif letr=='7' :
                num= numlist[7]
            elif letr=='8' :
                num= numlist[8]
            elif letr=='9' :
                num= numlist[9]
            
            elif letr=='+' :
                num= oplist[1]
            elif letr=='-' :
                num= oplist[2]
            else:
                print('fuck u and ur math')
                
            num.click()
        equal.click()
        
#------------------------------------------------------------------------------
oper= input('Type your operation: ')
        
#------------------------------------------------------------------------------
bot = DumbassBot()
bot.gocalc()
bot.traduct(oper)
#bot.defnum()      PREVIOUS ATTEMPT
        
        
        
        
        
        