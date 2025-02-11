import os
from seleniumbase import SB
from selenium.webdriver.common.by import By


# Getting data breach info
def _haveibeenpwned(email):
    with SB(uc=True, test=True, locale_code="en") as sb:
        url = "https://haveibeenpwned.com"
        sb.open(url)

        sb.type("#AccountCheck_Account", email)
        sb.click("#searchPwnage")

        # Handle CAPTCHA
        sb.uc_gui_click_captcha()

        # Wait for the breach results to load
        sb.wait_for_element_visible("#pwnedSites")

        # Find breach elements by CSS class
        breach_elements = sb.find_elements(By.CLASS_NAME, "pwnedSearchResult")
        breach_data = []

        for breach in breach_elements:
            breach_id = breach.get_attribute("id")
            if breach_id:
                breach_data.append({"title": breach_id})

        sb.save_screenshot_to_logs()
        return breach_data

# Returning data to frontend
def interface(firstName, lastName, email, phone):
    data = [firstName, lastName, email, phone]
    
    if email:
        # Getting breach list from haveibeenpwned
        breached = _haveibeenpwned(email)
        print(f"\n\nBREACH TYPE:\n {type(breached)} \n {breached}")
        return breached
    else:
        return data
