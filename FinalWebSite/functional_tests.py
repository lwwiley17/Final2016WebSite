# Boiler Plate


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
import os

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		if os.name=='nt':
			self.browser = webdriver.Chrome()
		else:
			self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_home_page(self):
		self.browser.get('http://localhost:8000/index.html')

		#1 Add a test for the title to the web site to be "The Mandelbrot Set" then add the title.
		self.assertIn("The Mandelbrot Set",self.browser.title)

		#2 Add a test for the header on the home page to be "The Mandelbrot Set" and then add the header.
		h=self.browser.find_element_by_tag_name('h1')

		#3 Add a test for the image M.jpg to be on the home page.
		m=self.browser.find_element_by_tag_name('img')
		self.assertIn('M.jpg',m.get_attribute('src'))

		#4 Add a test for a circular clickable area on the big center section of M.jpg.
		a=self.browser.find_element_by_id('homepage')
		a.click()
		
		#5 Add a test that clicking on it brings you to a page called "code.html"
		self.assertIn("Code",self.browser.title)

		#6 Add a test for the header on code.html to be "The Code"
		h=self.browser.find_element_by_tag_name('h1')

		#7 Add a test for mbrot.png in the code.html page.
		n=self.browser.find_element_by_tag_name('img')
		self.assertIn('mbrot.png',n.get_attribute('src'))

		#8 Add a test for a clickable area on mbrot.png similar to the one on M.jpg
		b=self.browser.find_element_by_id('code')
		b.click()

		#9 Add a test that it takes you back to the home page.
		self.assertIn("The Mandelbrot Set",self.browser.title)
		

if __name__=="__main__":
		unittest.main(warnings="ignore")

