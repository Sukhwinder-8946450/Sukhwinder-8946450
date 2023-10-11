# Importing required libraries

# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Amazon.ca homepage
driver.get("https:www.linkedin.com")
time.sleep(3)



Logininput = driver.find_element("id", "session_key")
Logininput.send_keys("psukhwinder880@gmail.com")
Passwordinput = driver.find_element("id","session_password")
Passwordinput.send_keys("0099sukh5942")

Signinbutton = driver.find_element(By.CSS_SELECTOR,"button.btn-md.btn-primary.flex-shrink-0.cursor-pointer.sign-in-form__submit-btn--full-width.w-full.max-w-\[400px\].mx-auto")
Signinbutton.click()

time.sleep(30)
#search_bar = driver.find_element(By.CSS_SELECTOR, "input.search-global-typeahead__input")
search_bar = driver.find_element(By.CSS_SELECTOR,"input.search-global-typeahead__input")
#search_bar = driver.find_element(By.CSS_SELECTOR,"input#search")

search_bar.send_keys("Software Quality Assurance and testing jobs")
search_bar.send_keys(Keys.ENTER)

time.sleep(7)

savebtn = driver.find_element(By.CSS_SELECTOR, ".search-results-container div:first-child .artdeco-card:nth-child(1)>.reusable-search__entity-result-list .reusable-search__result-container:first-child .entity-result:first-child .t-roman.t-sans:first-child a")
savebtn.click()


time.sleep(3)

jobBtn = driver.find_element(By.CSS_SELECTOR, ".job-details-jobs-unified-top-card__container--two-pane .jobs-s-apply .jobs-apply-button")
jobBtn.click()

time.sleep(3)

saveInBtn = driver.find_element(By.CSS_SELECTOR, ".job-details-jobs-unified-top-card__container--two-pane .jobs-save-button")
saveInBtn.click()

# Finding the search bar and entering text
# search_bar = driver.find_element_by_id("id","twotabsearchtextbox") old syntax
#search_bar = driver.find_element(By.CSS_SELECTOR,"input#search")
#search_bar.send_keys("sidhu mosse wala")

# Submitting the search query
#search_bar.send_keys(Keys.RETURN)

# Waiting for the search results page to load
time.sleep(10)
driver.close()
# Verifying that the search results page has loaded
#assert "sidhu" in driver.title


# Selecting a laptop from the search results
#laptop_link = driver.find_element("/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer[5]/div[3]/ytd-video-renderer[2]/div[1]/div/div[1]/div/h3/a")
#laptop_link.click()

time.sleep(30)


# Waiting for the laptop details page to load
time.sleep(5)

# Adding the laptop to the cart
#add_to_cart_button = driver.find_element("id","add-to-cart-button")
#add_to_cart_button.click()

# Waiting for the cart to update
time.sleep(5)

# Clicking on no thanks button
#no_thanks_button= driver.find_element("xpath","/html/body/div[9]/div[3]/div[1]/div/div/div[2]/div[2]/div/div/div[3]/div/span[2]/span/input")
#no_thanks_button.click()
time.sleep(2)

#proceed_to_checkout= driver.find_element("xpath","/html/body/div[1]/div[1]/div/div[1]/div[2]/div/div[3]/div/div[1]/form/span/span/span/input")
#proceed_to_checkout.click()
time.sleep(2)




# Verifying that the laptop has been added to the cart
# cart_count = driver.find_element("id","nav-cart-count")
# assert cart_count.text == "1"
# cart_count.click()

# Closing the webdriver
driver.close()
