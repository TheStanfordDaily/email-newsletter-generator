from urllib.parse import urlencode
from datetime import date

# What are the URL referral tracking parameters for this digest?
URL_PARAMS = {
    "utm_campaign": "digest",
    "utm_medium": "email",
    "utm_source": "mailchimp",
    "utm_content": date.today().strftime("%b-%d-%Y")
}


def formatted_url(url):
    return url + "?" + urlencode(URL_PARAMS)


def itemize(items):
    len_items = len(items)
    if len_items == 0:
        return ""
    elif len_items == 1:
        return items[0]
    return ", ".join(items[:-1]) + " and " + items[-1]