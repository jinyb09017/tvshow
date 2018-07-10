from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.key_actions import KeyActions
from selenium.webdriver.common.by import By

# import org.openqa.selenium.chrome.ChromeOptions
# options1 = webdriver.ChromeOptions()
# options1.add_argument("--start-fullscreen")
# options1.add_argument("disable-infobars")
# options1.add_argument("window-position=0,0")
# driver1 = webdriver.Chrome(chrome_options=options1)
# driver1.get("https://tv.apitops.com/web/screen1.html?key=24efd4320a094aeb9e192f41ca4c4b78")


# options = webdriver.ChromeOptions()
# options.add_argument("--start-fullscreen")
# options.add_argument("disable-infobars")
# options.add_argument("window-position=1920,0")
# driver = webdriver.Chrome(chrome_options=options)
#
# driver.get("https://tv.apitops.com/web/screen2.html?key=24efd4320a094aeb9e192f41ca4c4b78")
# driver.get("https://www.baidu.com")

siteUrls = ["https://tv.apitops.com/web/screen1.html?key=24efd4320a094aeb9e192f41ca4c4b78",
            "https://tv.apitops.com/web/screen2.html?key=24efd4320a094aeb9e192f41ca4c4b78"]

for index in range(len(siteUrls)):

    options = webdriver.ChromeOptions()
    options.add_argument("--start-fullscreen")
    options.add_argument("disable-infobars")
    if index == 0:
        options.add_argument("window-position=0,0")
        # 不知道为何必须初始两次才能运行时不中断
        driver = webdriver.Chrome(chrome_options=options)
        driver.get(siteUrls[index])
    else:
        options.add_argument("window-position=1920,0")
        driver1 = webdriver.Chrome(chrome_options=options)
        driver1.get(siteUrls[index])

    print siteUrls[index]

# driver = webdriver.Chrome()
# driver.

# driver.set_window_rect(1920, 0, 1920, 1080)
# driver.set_window_position(1920, 0)
# driver.maximize_window()

# driver.get("http://www.baidu.com")

# elem = driver1.find_element_by_name("wd")
# elem.clear()
# elem.send_keys("who is the best man")
# elem.send_keys(Keys.RETURN)
# # elem.send_keys(Keys.F11)
# #
# elem = driver.find_element_by_name("wd")
# elem.clear()
# elem.send_keys("hello world")
# elem.send_keys(Keys.RETURN)
# elem.send_keys(Keys.F11)

# driver.find_element_by_tag_name("body").sendKeys(Keys.F11);

# shortcutGoToFullScreen = Keys.chord(Keys.F11);
# driver.find_element_by_tag_name("body").send_keys(Keys.F11)
# driver.maximize_window()
#
# body = driver.find_element_by_tag_name('body')
# body.send_keys(Keys.F11)


# driver.get("http://www.baidu.com")
# driver.close()
# elem = driver.find_element_by_name("wd")
# elem.clear()
# elem.send_keys("this is a good test")
# elem.send_keys(Keys.RETURN)
# elem.send_keys(Keys.F11)

# driver.find_element_by_tag_name("body").sendKeys(Keys.F11);

# shortcutGoToFullScreen = Keys.chord(Keys.F11);
# driver.find_element_by_tag_name("body").send_keys(Keys.F11)
# driver.maximize_window()
#

# driver1 = webdriver.Firefox()
# driver1.get("http://www.baidu.com")
# body1 = driver1.find_element_by_tag_name('body')
# body1.send_keys(Keys.F11)
# driver.set_window_position(1920, 0)


#
# action = KeyActions(driver)
#
# action.send_keys(Keys.F11).perform()
# driver.find_element_by_tag_name(By.xpath('/html/body')).sendKeys(webdriver.Key.F11);
