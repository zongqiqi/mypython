# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.proxy import ProxyType
from selenium.webdriver.common.action_chains import ActionChains
import time
import requests
import json
r = requests.get('http://127.0.0.1:8000/?types=0&count=5&country=国内')
ip_ports = json.loads(r.text)
print ip_ports
ip = ip_ports[0][0]
port = ip_ports[0][1]
print ip,port

profile = webdriver.FirefoxProfile()
profile.set_preference('network.proxy.type', 1)
profile.set_preference('network.proxy.http', ip)
profile.set_preference('network.proxy.http_port', port)  # int
profile.update_preferences()
driver = webdriver.Firefox(firefox_profile=profile)
driver.get('http://4xqn5l.v.tp8.me/')
time.sleep(30)
toupiao = driver.find_element_by_id('cphMainContent_rptTopicList_rptOptions_0_hplOneKeyVote_39').click()
print 'dianji'
# ActionChains(driver).context_click(toupiao).perform()
time.sleep(10)
driver.quit()