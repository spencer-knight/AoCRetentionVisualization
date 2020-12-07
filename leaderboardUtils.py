from selenium import webdriver
from selenium.webdriver.chrome.options import Options

##### Notes #####
# https://adventofcode.com/2020/stats
# <pre class="stats"> The days </pre>
# Each day is an <a> tag
# href="/<year>/day/<day>"
# text is also the day
# span class="stats-both"
# span class="stats-firstonly"
# text is either stars or the number ^^
##### /Notes #####

# Selenium setup, change PATH to your chromedriver path. Obviously.
PATH = "./chromedriver.exe"
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')  
driver = webdriver.Chrome(PATH, chrome_options=options)

def getLeaderboard():
    dayInfo = []
    driver.get( "https://adventofcode.com/2020/stats")
    aTags = driver.find_elements_by_tag_name("a")
    for a in aTags:
        if '*' in a.text:
            dayInfo.append( a.text.split())
    dayInfo = sorted(dayInfo, key = lambda day: int(day[0]))

    return dayInfo
    #print( dayInfo)