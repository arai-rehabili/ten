from selenium import webdriver
from time import sleep

def __init__(self):
    print("init")

def challenge(driver, stoptime):
    button = driver.find_element_by_id("button")
    # start
    button.click()
    print("start")
    sleep(stoptime)
    # stop
    button.click()
    print("stop")

    # string to float convert is result
    result = driver.find_element_by_id("count").text

    if result == "10.00":
        print("結果10.00秒")
        print("Success!")
        sleep(20)
        exit()
    print("結果" + str(result) + "秒")
    result = float(result)

    sleep(1)
    # reset
    button.click()
    return result

def process():
    # open driver
    driver = webdriver.Chrome("chromedriver.exe")
    # open browser
    driver.get("https://totoraj930.github.io/10sec/")
    sleep(4.000)

    # init challenge info
    time = 10.000
    gapTime = "start"

    # challenge roop to "result == 0"
    while gapTime != 0:
        # return : challenge time
        gapTime = 10.000 - challenge(driver, time)
        print("ズレ" + str(gapTime) + "秒を修正して再挑戦")
        # tuning time
        time = time + gapTime

if __name__ == "__main__":
    process()
