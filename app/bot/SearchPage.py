from bot.base import BasePage
from bot.locators import SearchResultPageLocators
from utils.db.insert import insert as insert_to_db
from utils.config.env import SITE_NAME


class SearchPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(SearchResultPageLocators.URL)
        self.i = 0

    def get_total_results(self):
        x = self.get_element(
            *SearchResultPageLocators.TOTAL_RESULT_FOUND).text
        total = int(x.split(' ')[0].replace(',', ''))
        return total

    def get_item_box(self):
        self.item_box = self.get_elements(*SearchResultPageLocators.ITEM_BOX)
        return self.item_box

    def count_item_box(self):
        try:
            return len(self.item_box)
        except:
            return len(self.get_item_box())

    def insert_item_price_pair_into_mongo_db(self, site="ebay"):

        if len(self.get_item_box()) < 1:
            return

        cols = []

        for item in self.item_box:
            # print('-'*100, item, type(item))
            try:
                self.i += 1
                id_, name, price = str(self.i), item.find_element(
                    *SearchResultPageLocators.ITEM_NAME).text, item.find_element(*SearchResultPageLocators.ITEM_PRICE).text

                name, price = name.encode(
                    "ascii", "ignore"), price.encode("ascii", "ignore")
                name, price = name.decode(), price.decode()
                temp = {"id": id_, "item_name": name,
                        "price": price, "site": SITE_NAME}
                cols.append(temp)

            except Exception as e:
                print(e)

        # Insert
        try:
            # insert.insert(data=cols, db_name='ebay_db', collection_name='items')
            insert_to_db(data=cols)
        except Exception as e:
            print(e)

    def is_next_page_button_found(self):
        try:
            self.get_element(*SearchResultPageLocators.NEXT_PAGE_BUTTON)
            return True
        except Exception as e:
            print(e)
            return False

    def click_next_page(self):
        self.get_element(*SearchResultPageLocators.NEXT_PAGE_BUTTON).click()
        # self.driver
