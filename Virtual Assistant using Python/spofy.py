from selenium import webdriver

class song():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='C:\webdrivers/chromedriver.exe')

    def sing(self ,query):
        self.query=query
        self.driver.get(url="https://open.spotify.com/search/" + query)
        s = self.driver.find_element_by_xpath('//*[@id="searchPage"]/div/div/section[1]/div[2]/div/div/div/div[3]/button')
        s.click()
        #spo=self.driver.find_element_by_xpath('/html/body/app-root/app-home/div[2]/div/song-info/div/div[1]/div[3]/div[2]/div[1]/button[1]')
        #spo.click()

