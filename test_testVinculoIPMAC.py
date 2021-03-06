# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTestVinculoIPMAC():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_testVinculoIPMAC(self):
    self.driver.get("https://emulator.tp-link.com/C50V4_BR_Emulator/Emulator/index.htm")
    self.driver.set_window_size(1054, 808)
    self.driver.switch_to.frame(0)
    self.driver.switch_to.frame(1)
    self.driver.find_element(By.CSS_SELECTOR, "#menu_arp > span").click()
    self.driver.switch_to.default_content()
    self.driver.switch_to.frame(2)
    self.driver.find_element(By.ID, "arpBind_en").click()
    self.driver.find_element(By.CSS_SELECTOR, ".T_addnew").click()
    self.driver.find_element(By.ID, "macAddr").click()
    self.driver.find_element(By.ID, "macAddr").send_keys("0A:00:27:00:00:11")
    self.driver.find_element(By.ID, "ipAddr").click()
    self.driver.find_element(By.ID, "ipAddr").send_keys("192.168.56.1")
    self.driver.find_element(By.ID, "saveBtn").click()
  
