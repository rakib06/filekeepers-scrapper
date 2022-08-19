from bot.base import BasePage
from bot.locators import SearchResultPageLocators


class SearchPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(SearchResultPageLocators.URL)
        self.i = 1

    def get_total_items(self):
        self.item_name_list = self.get_elements(
            *SearchResultPageLocators.ITEM_NAME)
        return self.item_name_list

    def count_total_items(self):
        return len(self.get_total_items())

    def get_total_prices(self):
        self.item_price_list = self.get_elements(
            *SearchResultPageLocators.ITEM_PRICE)
        return self.item_price_list

    def count_total_prices(self):
        return len(self.get_total_prices())

    def is_item_price_pair_matched(self):
        return self.count_total_items() == self.count_total_prices()

    def get_item_price_pair(self):
        if self.is_item_price_pair_matched():
            return zip(self.item_name_list, self.item_price_list)
        else:
            return None

    def save_item_price_pair(self, filename="test.txt"):
        if self.get_item_price_pair() is None:
            print("No item-price pair found!")
            return
        for item in self.get_item_price_pair():
            with open(filename, 'a+') as f:
                try:
                    x = str(self.i) + ". " + item[0].text + \
                        ": Price = " + item[1].text + "\n"
                    x = x.encode("ascii", "ignore")
                    x = x.decode()
                    # print(x, type(x))
                    f.write(x)

                except Exception as e:
                    print(e)
            self.i += 1

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
