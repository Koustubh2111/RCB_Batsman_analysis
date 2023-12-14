# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 12:37:45 2021

@author: Owner
"""

def get_commentary_card_info(card):
    commentary_split = card.text.split('\n')
    #print(commentary_split)
    #Avoid unnecessary commentary
    if len(commentary_split) > 4:
                commentary_split = commentary_split[:-1]
            
    #Make sure it is a commnetary and not a end of over, injury or a delay in the game
    try:
        over = float(commentary_split[0])
    except:
        return None
    else:
         bowler = commentary_split[2].split('to')[0]
        
         batter = commentary_split[2].split('to')[1].split(',')[0]
        
         return [{'Over' : float(commentary_split[0]),                  'Runs Scored' : commentary_split[1],                  'Bowler' : bowler,                  'Batsman' : batter,                  'commentary' : commentary_split[-1]}]
        
def get_match_info(driver):
        
    #get team names and totals
    team1 = driver.find_element_by_xpath        ('/html/body/div[1]/section/section/div[1]/div/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div/div/div[3]/div[1]/div[1]/a/p').text

    team1_total = driver.find_element_by_xpath        ('/html/body/div[1]/section/section/div[1]/div/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div/div/div[3]/div[1]/div[2]/span[2]').text

    team2 = driver.find_element_by_xpath        ('/html/body/div[1]/section/section/div[1]/div/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div/div/div[3]/div[2]/div[1]/a/p').text

    team2_total = driver.find_element_by_xpath        ('/html/body/div[1]/section/section/div[1]/div/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div/div/div[3]/div[2]/div[2]/span[2]').text

    date = driver.find_element_by_xpath            ('/html/body/div[1]/section/section/div[1]/div/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div/div/div[2]').text.split(',')[2]


    return [{'Team_Batting_First_Total' : [team1, team1_total],              'Team_Batting_Second' : [team2, team2_total],              'Date' : date}]
    
def click_on_next_innings():
    
    scroll_up(driver)
    
    #Click on down arrow
    driver.find_element_by_css_selector    ('#main-container > div:nth-child(1) > div > div.container > div.row > div.col-16.col-md-16.col-lg-12.main-content-x > div.match-body > div.comment-container > div.comment-container-head > div.dropdown-container.comment-inning-dropdown > button > i')    .click()
    
    #Select the team above for first innings
    driver.find_element_by_css_selector    ('#main-container > div:nth-child(1) > div > div.container > div.row > div.col-16.col-md-16.col-lg-12.main-content-x > div.match-body > div.comment-container > div.comment-container-head > div.dropdown-container.comment-inning-dropdown > div > div > ul > li:nth-child(1)')    .click()
    
    scroll_down(driver)
    scroll_up(driver)
    
def get_all_commentary_card_info_page(match_url):
    
    #Get the commentary info for both innings of a match
 
    #sleep
    print('Wait 5s for page loading')
    time.sleep(5)
    
    #Get details of the match
    try:
        print('    Get match Info')
        match_info = get_match_info(driver)
    except:
        return None
    
    #Scrape the data for the second innings
    print('    Scrape second innings')
    commentary_cards_second_innings = driver.find_elements_by_class_name('match-comment')    
    second_innings_info = []
    for card in commentary_cards_second_innings:        
        second_innings_info.append(get_commentary_card_info(card))
        
    #Click to first innings
    print('    Navigate to first innings')
    click_on_next_innings()
    
    #Scrape the data for the first innings
    print('    Scrape first innings')
    commentary_cards_first_innings = driver.find_elements_by_class_name('match-comment')
    first_innings_info = []
    for card in commentary_cards_first_innings:        
        first_innings_info.append(get_commentary_card_info(card))
        
    return [match_info, first_innings_info, second_innings_info]

def scroll_down(driver):

    #https://stackoverflow.com/questions/48850974/selenium-scroll-to-end-of-page-in-dynamically-loading-webpage
    
    
    # Get scroll height.
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:

        # Scroll down to the bottom.
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load the page.
        time.sleep(2)

        # Calculate new scroll height and compare with last scroll height.
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:

            break

        last_height = new_height
        
def scroll_up(driver):

    #https://stackoverflow.com/questions/48850974/selenium-scroll-to-end-of-page-in-dynamically-loading-webpage
    
    
    # Get scroll height.
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:

        # Scroll down to the bottom.
        driver.execute_script("window.scrollTo(document.body.scrollHeight, 0);")

        # Wait to load the page.
        time.sleep(2)

        # Calculate new scroll height and compare with last scroll height.
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:

            break

        last_height = new_height

    
    

options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-infobars")
options.add_argument("--disable-extensions")
options.add_experimental_option("prefs", 
{"profile.default_content_setting_values.notifications": 2 
 })
driver = webdriver.Chrome(options = options)


global_data = []
for year_url in BalltoBallURL_dict:
    for match_url in year_url:
        
        #Open the page
        print('Open match url : ', match_url)
        driver.get(match_url)
        
        #Scroll down to load everything 
        scroll_down(driver)
        scroll_up(driver)
        
        #Get match all info
        global_data.append(get_all_commentary_card_info_page(match_url))