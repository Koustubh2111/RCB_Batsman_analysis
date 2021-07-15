# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 12:18:20 2021

@author: Owner
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys #Access to enter/esc key
from selenium.webdriver.chrome.options import Options #Not open the browser while running
import time


def OpenBowlerPage(bowler_name, website):
    
    #website = iplt20 or cricinfo
    
    search = driver.find_element_by_name("q")
    search.send_keys(bowler_name + website)
    search.send_keys(Keys.RETURN)
    driver.find_element_by_tag_name("cite").click()
    
def getBowlerStat(bowler_name):
    
    #Open the bowler page in iplt20.com
    OpenBowlerPage(bowler_name, " iplt20")
    
    #delay for 2seconds
    #time.sleep(1)
    
    #Scrape the final table corresponding to bowler stats
    try:
        
        bowling_stats_table = driver.find_elements_by_tag_name('table')[-1]
        
    except:
        
        return []
    
 
    #Each field is a row with the first two rows being headers and aggergates
    bowler_stat = []
    for rows in bowling_stats_table.find_elements_by_tag_name('tr')[2:]:
        
        fields = rows.find_elements_by_tag_name('td')
    
        rows_stat = [field.text for field in fields]
        
        bowler_stat.append({rows_stat[0] : dict(zip(bowler_keys, rows_stat[1:])) })
    
    
    return bowler_stat

def getNonStrikerStat(non_striker_name):
    
    OpenBowlerPage(non_striker_name, " iplt20")
    
    try:
        
        non_striker_stats_table = driver.find_elements_by_tag_name('table')[-2]
        
    except:
        
        return []
    non_striker_stat = []
    for rows in non_striker_stats_table.find_elements_by_tag_name('tr')[2:]:
        
        fields = rows.find_elements_by_tag_name('td')
    
        rows_stat = [field.text for field in fields]
        
        non_striker_stat.append({rows_stat[0] : dict(zip(batsman_keys, rows_stat[1:])) })
        
    return non_striker_stat
    
    
    
def getBowlerType(bowler_name):
    
    #Open the bowler profile in cricbuzz; iplt20 is incomplete
    OpenBowlerPage(bowler_name, " profile cricbuzz")
    
    try:
        #Get web element of bowler type
        bowler_type = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div[2]/div[1]/div/div[13]')
    except:
        return
    
    return bowler_type.text