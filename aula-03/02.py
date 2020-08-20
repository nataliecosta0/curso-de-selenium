"""
Crie um programa com selenium que:
	* Jogue o jogo
	* Quando você ganhar o script deve parar de ser executado

url: https://curso-python-selenium.netlify.app/exercicio_02.html
"""
from selenium.webdriver import Firefox
from time import sleep

url = 'https://curso-python-selenium.netlify.app/exercicio_02.html'
browser = Firefox()
browser.get(url)
sleep(7)

how_to_play, expect_number_text = browser.find_elements_by_tag_name('p')
expect_number = expect_number_text.text.split()
expect_position_number = (f"Você ganhou: {expect_number[2]}")

click_here = browser.find_element_by_partial_link_text('clique')
number_give_from_game = 0

while expect_position_number != number_give_from_game:
	click_here.click()
	number = browser.find_elements_by_tag_name('p')
	for num in number:
		number_give_from_game = num.text

browser.quit()