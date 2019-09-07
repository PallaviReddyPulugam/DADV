#!/usr/bin/env python
# coding: utf-8

# In[30]:


from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select,WebDriverWait
driver=webdriver.Chrome(executable_path='\chromedriver.exe')
driver.get("http://www.eciresults.nic.in")
link = driver.find_element_by_link_text('Partywise')
link.click()
states=[]
select1= Select(driver.find_element_by_xpath( "//select[@id='ctl00_ContentPlaceHolder1_Result1_ddlState']"))
states=["Andhra"+" "+"Pradesh","Telangana"]



i={}
import csv   
fields=['Party','Total','State']
    
#file_path=r'Downloads\test.csv'
with open(r'Downloads\state.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        
          
                
                    
                #print(row)
    csvwriter.writerow(fields)



for state in states:
    print(state)
   
"""for state in states:
    #cons=[]
    select1= Select(driver.find_element_by_xpath("//select[@id='ctl00_ContentPlaceHolder1_Result1_ddlState']"))   
    select1.select_by_visible_text(state)
    
   
    #select2= Select(driver.find_element_by_xpath( "//select[@id='ddlAC']")) 
     
    
for k,v in i.items():
        print(k,v)
        print()
"""       
#data={}        
for state in states:
    select1= Select(driver.find_element_by_xpath( "//select[@id='ctl00_ContentPlaceHolder1_Result1_ddlState']"))   
    select1.select_by_visible_text(state)
    
    table_id=driver.find_elements_by_tag_name('table')[-2]
    
    rows=table_id.find_elements_by_tag_name('tr')
    for row in rows[4:]:
    # Get the columns (all the column 2)
        #print(row)
        col0 = row.find_elements_by_tag_name('td')[0]
        col3 = row.find_elements_by_tag_name('td')[3]
        
        
           
           # print(col1.text) #prints text from the element
            #print(col2.text)
            #print(col3.text)
            
        
        listdata=[]
        listdata.append(col0.text)
        listdata.append(col3.text)
        listdata.append(state)
               
        with open(r'Downloads\state.csv', 'a', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        
          
                
                    
                #print(row)
                
            csvwriter.writerow(listdata)
                        


# In[ ]:





# In[ ]:




