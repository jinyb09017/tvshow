from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.key_actions import KeyActions
from selenium.webdriver.common.by import By


def openChrome(url, positionStr):
    options1 = webdriver.ChromeOptions()
    options1.add_argument("--start-fullscreen")
    options1.add_argument("disable-infobars")
    options1.add_argument(positionStr)
    driver1 = webdriver.Chrome(chrome_options=options1)
    # driver1.get("https://www.baidu.com")
    print driver1
    print options1
    driver1.get(url)


def getPosition(pos):
    screenWidth = 1920
    postion = pos * screenWidth
    positionLeft = "window-position="
    positionRight = ",0"
    positionStr = positionLeft + str(postion) + positionRight
    print positionStr
    return positionStr


def showTv():
    siteUrls = ["https://tv.apitops.com/web/screen1.html?key=24efd4320a094aeb9e192f41ca4c4b78",
                "https://tv.apitops.com/web/screen2.html?key=24efd4320a094aeb9e192f41ca4c4b78"]

    for index in range(len(siteUrls)):
        positionStr = getPosition(index)
        url = siteUrls[index]
        openChrome(url, positionStr)

    # if __name__ == '__main__':

openChrome("https://tv.apitops.com/web/screen1.html?key=24efd4320a094aeb9e192f41ca4c4b78", "window-position=0,0")
openChrome("https://tv.apitops.com/web/screen2.html?key=24efd4320a094aeb9e192f41ca4c4b78", "window-position=1920,0")
