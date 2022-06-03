from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.basketball-reference.com/leagues/NBA_1978_games-october.html")
print("title is: "+driver.title)
search = driver.find_element_by_class_name("suppress_glossary sortable stats_table now_sortable")
print(search)
driver.quit()