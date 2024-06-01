import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import time, os

class Twitterbot:

	def __init__(self, email, password):
		
		webdriver_path = os.path.join(os.getcwd(), 'chromedriver.exe') 
		service = Service(webdriver_path)
		service.start()

		self.email = email
		self.password = password

		options = ChromeOptions()
		options.add_argument("--start-maximized")
		options.add_experimental_option("excludeSwitches", ["enable-automation"])

		proxy_address = "us-ca.proxymesh.com:31280"
		options.add_argument(f"--proxy-server={proxy_address}")

		self.bot = webdriver.Chrome(
			service=service,
			options = options
		)

	def login(self):

		bot = self.bot
	
		url = "https://twitter.com/i/flow/login"
		bot.get(url)
		
		username = WebDriverWait(bot, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[autocomplete="username"]')))
		username.send_keys(self.email)
		username.send_keys(Keys.ENTER)

		password = WebDriverWait(bot, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="password"]')))
		password.send_keys(self.password)
		password.send_keys(Keys.ENTER)

		time.sleep(2)



	def getTrendingTopics(self):
		bot = self.bot
		try:
			
			trending_topics_section = WebDriverWait(bot, 10).until(
				EC.presence_of_element_located((By.XPATH, '//div[@aria-label="Timeline: Trending now"]'))
			)

	
			trending_topics_list = trending_topics_section.find_elements(By.XPATH, './/div[@data-testid="trend"]')

		
			print(f"Number of trending topics found: {len(trending_topics_list)}")

	
			top_5_trending_topics = []
			for topic in trending_topics_list[:5]:
				try:
					
					topic_text = None
					try:
						topic_text = topic.find_element(By.XPATH, './/div[contains(@dir,"ltr")]/span/span').text
					except Exception:
						try:
							
							topic_text = topic.find_element(By.XPATH, './/div[@dir = "ltr" and @class="css-146c3p1 r-bcqeeo r-1ttztb7 r-qvutc0 r-37j5jr r-a023e6 r-rjixqe r-b88u0q r-1bymd8e" ]/span').text
						except Exception:
							return e

					if topic_text:
						top_5_trending_topics.append(topic_text)
					else:
						print("No text found for this topic element")

				except Exception as e:
					return e

		
			return top_5_trending_topics

		except Exception as e:
			return e


