# coding:utf-8
from selenium import webdriver


class Chrome:
    def __init__(self, key):
        self.key = key

    def open_web_up(self):
        #
        siteUrls = ["https://tv.apitops.com/web/screen3.html",
                    "https://tv.apitops.com/web/screen2.html",
                    "https://tv.apitops.com/web/screen1.html"]


        for index in range(len(siteUrls)):

            url = siteUrls[index] + "?key=" + self.key
            options = webdriver.ChromeOptions()
            options.add_argument("--start-fullscreen")
            options.add_argument("disable-infobars")
            options.add_argument("--allow-running-insecure-content")
            if index == 0:
                options.add_argument("window-position=-3840,0")
            elif index == 1:
                options.add_argument("window-position=-1920,0")
            elif index == 2:
                options.add_argument("window-position=0,0")

            print url
            driver = webdriver.Chrome(chrome_options=options)
            driver.get(url)



    def open_web_down(self):

        siteUrls = ["https://tv.apitops.com/web/screen4.html",
                    "https://tv.apitops.com/web/screen5.html",
                    "https://tv.apitops.com/web/screen6.html"]

        for index in range(len(siteUrls)):

            url = siteUrls[index] + "?key=" + self.key
            options = webdriver.ChromeOptions()
            options.add_argument("--start-fullscreen")
            options.add_argument("disable-infobars")
            options.add_argument("--allow-running-insecure-content")
            if index == 0:
                options.add_argument("window-position=0,0")
            elif index == 1:
                options.add_argument("window-position=1920,0")
            elif index == 2:
                options.add_argument("window-position=3840,0")

            print url
            driver = webdriver.Chrome(chrome_options=options)
            driver.get(url)


