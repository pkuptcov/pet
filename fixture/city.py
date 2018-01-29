import time


class CityHelper:

    def __init__(self, app):
        self.app = app

    def city_change_msk(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("div.top_region").click()
        time.sleep(1)
        wd.find_element_by_link_text("Москва").click()

    def city_change_nov(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("div.top_region").click()
        time.sleep(1)
        wd.find_element_by_link_text("Великий Новгород").click()

    def city_change_vbg(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("div.top_region").click()
        time.sleep(1)
        wd.find_element_by_link_text("Выборг").click()

    def city_change_gtn(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("div.top_region").click()
        time.sleep(1)
        wd.find_element_by_link_text("Гатчина").click()

    def city_change_lug(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("div.top_region").click()
        time.sleep(1)
        wd.find_element_by_link_text("Луга").click()

    def city_change_kgs(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("div.top_region").click()
        time.sleep(1)
        wd.find_element_by_link_text("Кингисепп").click()

    def city_change_pzv(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("div.top_region").click()
        time.sleep(1)
        wd.find_element_by_link_text("Петрозаводск").click()

    def city_change_tvr(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("div.top_region").click()
        time.sleep(1)
        wd.find_element_by_link_text("Тверь").click()

    def city_change_spb(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("div.top_region").click()
        time.sleep(1)
        wd.find_element_by_link_text("Санкт-Петербург").click()