'''import time


class CityHelper:


    def __init__(self, app):
        self.app = app


    def city_change(self):
    wd = self.app.wd
    wd.find_element_by_css_selector("div.top_region").click()
    time.sleep(1)
    wd.find_element_by_link_text("Москва").click()'''