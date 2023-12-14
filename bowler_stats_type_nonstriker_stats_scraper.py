# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 12:22:51 2021

@author: Owner
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from iplt20_scraping_helper import OpenBowlerPage, getBowlerStat, getNonStrikerStat, getBowlerType
import time
import json


bowler_keys = ['Matches',
               'Balls',          
               'Runs',          
               'Wickets',          
               'Best Bowling',          
               'Average',          
               'Economy',          
               'Strike Rate',          
               '4 Wicket Hauls',          
               '5 Wicket Hauls']

batsman_keys = ['Matches',                 
                'NotOut',                 
                'Runs',                 
                'Highest Score',                 
                'Average',                 
                'Balls faced',                 
                'Strike rate',                 
                '100s',                 
                '50s',                 
                'Fours',                 
                'Sixes',                 
                'Catches',                 
                'Stumpings']


#All bowlers faced by ABD
all_bowlers = ['Sandeep Sharma', 'MM Sharma', 'VR Aaron', 'T Natarajan',
       'MP Stoinis', 'AR Patel', 'HH Pandya', 'KH Pandya', 'JJ Bumrah',
       'MJ McClenaghan', 'SN Thakur', 'JD Unadkat', 'DT Christian',
       'BA Stokes', 'Imran Tahir', 'UT Yadav', 'NM Coulter-Nile',
       'Basil Thampi', 'AJ Tye', 'RA Jadeja', 'Ankit Soni', 'DL Chahar',
       'LH Ferguson', 'SL Malinga', 'KV Sharma', 'CR Woakes', 'SP Narine',
       'Kuldeep Yadav', 'MG Johnson', 'PP Chawla', 'AD Russell', 'N Rana',
       'Mujeeb Ur Rahman', 'R Ashwin', 'S Gopal', 'B Laughlin',
       'S Nadeem', 'CH Morris', 'HV Patel', 'R Tewatia', 'TA Boult',
       'Harbhajan Singh', 'SR Watson', 'DJ Bravo', 'Rashid Khan',
       'Shakib Al Hasan', 'S Lamichhane', 'A Mishra', 'CJ Dala', 'S Kaul',
       'K Gowtham', 'JC Archer', 'IS Sodhi', 'M Markande',
       'Mohammad Nabi', 'M Prasidh Krishna', 'I Sharma', 'K Rabada',
       'Mohammed Shami', 'M Ashwin', 'SM Curran', 'JP Behrendorff',
       'RD Chahar', 'AS Rajpoot', 'GC Viljoen', 'SE Rutherford',
       'KK Ahmed', 'B Kumar', 'JL Pattinson', 'KA Pollard', 'DR Sams',
       'A Nortje', 'SS Cottrell', 'Ravi Bishnoi', 'TK Curran',
       'Kartik Tyagi', 'Abhishek Sharma', 'KL Nagarkoti', 'CV Varun',
       'PJ Cummins', 'MJ Santner', 'Monu Kumar', 'JO Holder', 'M Jansen',
       'Avesh Khan', 'Harpreet Brar', 'R Vinay Kumar', 'M Muralitharan',
       'S Sreesanth', 'RP Singh', 'RV Gomez', 'AG Murtaza',
       'JEC Franklin', 'MM Patel', 'MS Gony', 'JA Morkel', 'S Randiv',
       'SB Jakati', 'SK Raina', 'TG Southee', 'Yuvraj Singh', 'R Sharma',
       'Kamran Khan', 'JD Ryder', 'AC Thomas', 'L Ablish', 'RJ Harris',
       'R McLaren', 'JH Kallis', 'Iqbal Abdulla', 'L Balaji', 'P Kumar',
       'SJ Srivastava', 'PC Valthaty', 'AN Ahmed', 'DE Bollinger',
       'DAJ Bracewell', 'GJ Maxwell', 'M Morkel', 'IK Pathan', 'B Lee',
       'R Bhatia', 'Pankaj Singh', 'GB Hogg', 'SK Trivedi', 'A Nehra',
       'AD Mathews', 'AB Dinda', 'P Awana', 'Harmeet Singh',
       'Azhar Mahmood', 'A Chandila', 'KK Cooper', 'DJ Hussey',
       'Anand Rajan', 'V Pratap Singh', 'A Ashish Reddy', 'DW Steyn',
       'PJ Sangwan', 'DP Nannes', 'JP Faulkner', 'MR Marsh',
       'DS Kulkarni', 'STR Binny', 'BAW Mendis', 'NLTC Perera',
       'CL White', 'YK Pathan', 'SMSM Senanayake', 'MG Neser', 'Z Khan',
       'PP Ojha', 'KW Richardson', 'R Dhawan', 'DJG Sammy',
       'Shivam Sharma', 'PV Tambe', 'JP Duminy', 'Parvez Rasool',
       'S Badree', 'KC Cariappa', 'RS Bopara', 'IC Pandey', 'DJ Hooda',
       'Karanveer Singh', 'Anureet Singh', 'J Suchith', 'MC Henriques',
       'Ankit Sharma', 'Mustafizur Rahman', 'P Negi', 'CR Brathwaite',
       'BB Sran', 'A Zampa', 'S Kaushik', 'DR Smith', 'KJ Abbott',
       'Bipul Sharma']


#Non strikers with ABD
all_non_strikers = ['Vishnu Vinod', 'KM Jadhav', 'Mandeep Singh', 'STR Binny',
       'V Kohli', 'CH Gayle', 'TM Head', 'Q de Kock', 'CJ Anderson',
       'PA Patel', 'MM Ali', 'SN Khan', 'C de Grandhomme', 'SO Hetmyer',
       'S Dube', 'MP Stoinis', 'AD Nath', 'D Padikkal', 'JR Philippe',
       'Washington Sundar', 'AJ Finch', 'Gurkeerat Singh', 'NA Saini',
       'GJ Maxwell', 'Shahbaz Ahmed', 'DT Christian', 'KA Jamieson',
       'HV Patel', 'RM Patidar', 'DR Sams', 'MA Agarwal', 'SS Tiwary',
       'AUK Pathan', 'TM Dilshan', 'CA Pujara', 'JJ van der Wath',
       'M Kaif', 'A Mithun', 'KB Arun Karthik', 'LA Pomersbach',
       'DL Vettori', 'R Vinay Kumar', 'AB McDonald', 'J Syed Mohammad',
       'R Rampaul', 'MC Henriques', 'Yuvraj Singh', 'JA Morkel',
       'RR Rossouw', 'MA Starc', 'S Rana', 'VH Zol', 'DJG Sammy',
       'SA Abbott', 'KD Karthik', 'D Wiese', 'SR Watson', 'KL Rahul',
       'Sachin Baby', 'Iqbal Abdulla']

all_bowler_stats = []

chrome_options = Options()
chrome_options.page_load_strategy = 'normal'

driver = webdriver.Chrome(options = chrome_options)
driver.implicitly_wait(10)

driver.get('https://www.google.com/')

#%%
#Get bowler stats from iplt20.com
time_bowler = []
for bowler_name in all_bowlers:    
    #Scrape Data 
    start = time.time()    
    #Not all of them have stats
    bowler_stat = getBowlerStat(bowler_name)    
    stop = time.time()    
    time_bowler.append(stop - start)
    print('Bowler : ' + bowler_name  ,stop - start)    
    #Use same tab
    driver.get('https://www.google.com/')
    #Append as dict with bowler name
    all_bowler_stats.append({bowler_name : bowler_stat})
driver.quit()

with open('bowler_stats.json', 'w') as f:
    json.dump(all_bowler_stats, f)

#%%
#Get bowler type of all bowler who bowled to ABD
time_bowler_type = []
all_bowler_type = []
driver = webdriver.Chrome()
driver.get('https://www.google.com/')
 
#ISSUE: More than 25bowlers, google recaptcha is thrown, JOB: FIX THIS!!
#Manual intervention is necessary when recpatcha is thrown, change the array index when continuing 
for bowler_name in all_bowlers:    
    #Scrape Data 
    start = time.time()    
    #Not all of them have stats        
    bowler_type = getBowlerType(bowler_name)    
    stop = time.time()    
    time_bowler_type.append(stop - start)
    print('Bowler : ' + bowler_name  ,stop - start)    
    #Use same tab
    driver.get('https://www.google.com/')
    #Append as dict with bowler name
    all_bowler_type.append({bowler_name : bowler_type})
driver.quit()

#%%
all_non_strikers_stat = []
driver = webdriver.Chrome()
driver.get('https://www.google.com/')

#Get non striker data with ABD

#Same issue as previous cell with the recpacha JOB: FIX
for non_striker in all_non_strikers:     
    start = time.time()    
    non_striker_stat = getNonStrikerStat(non_striker)    
    stop = time.time()
    print('Non Striker : ' + non_striker  ,stop - start)    
    all_non_strikers_stat.append({non_striker : non_striker_stat})    
    driver.get('https://www.google.com/')
driver.quit()
with open('non_striker_stat.json', 'w') as f:
    json.dump(all_non_strikers_stat, f)    

