import time
from bot.SearchPage import SearchPage
from bot import driver_setup

driver = driver_setup.local()


x = SearchPage(driver)
driver.maximize_window()

page_count = 1
max_page_count = 10

# x.scroll_down()
# print(x.count_total_items())
# print(x.count_total_prices())
# x.save_item_price_pair()
# x.click_next_page()


while (x.is_next_page_button_found() and page_count < max_page_count):
    print(f"Page {page_count} started")
    if x.is_item_price_pair_matched():
        print(f"Page {page_count} item -price pair matched ")
        x.save_item_price_pair()

    x.click_next_page()
    page_count += 1

time.sleep(10)
driver.quit()
