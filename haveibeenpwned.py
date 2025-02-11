from seleniumbase import SB

def haveibeenpwned(email):

    with SB(uc=True, test=True, locale_code="en") as sb:
        url = "https://haveibeenpwned.com"
        #sb.activate_cdp_mode(url)
        
        sb.open(url)
        sb.type("#AccountCheck_Account", email)
        sb.click("#searchPwnage")

        #recapcha being useless
        sb.uc_gui_click_captcha()
        sb.sleep(2)
        
        sb.wait_for_element_visible("#pwnedSites")
        
        breachList = sb.get_text("#pwnedSites")
        if breachList:
            print("Breaches found:")
            print(breachList)
        else:
            breachList = "Not pwned"
            print("No breaches found for this account.")

        sb.save_screenshot_to_logs()
    return breachList

#get from backend.py
email = "ezraibaldwin@gmail.com"
haveibeenpwned(email)
