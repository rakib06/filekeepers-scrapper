app/.env
```env
USE_DOCKER = True
URL = https://www.ebay.com/b/Desktops-All-In-One-Computers/171957/bn_1643067?_dmd
SCREENSHOT_DIR = local/screenshot/
LOGS_DIR = local/logs/ 
DATA_DIR = local/data/
ITEM_XPATH = "*//h3[@class= 's-item__title s-item__title--has-tags' or @class= 's-item__title']"
PRICE_XPATH = "*//span[@class='s-item__price']"
NEXT_PAGE_XPATH = "//*[@class='pagination__next icon-link']"
TOTAL_RESULT_FOUND_XPATH = "*//div/h2[@class='srp-controls__count-heading']"
ITEM_BOX_XPATH = "*//div[@class='s-item__wrapper clearfix']"
```