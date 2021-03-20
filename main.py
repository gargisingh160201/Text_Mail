from sample_test_cases import hotmail_outlook, gmail_mailspring
from bs4 import BeautifulSoup
import json


def trim_the_mail(mail_content: str, mail_client: str):
    # mail_content
    if not mail_content:
        return mail_content

    soup = BeautifulSoup(mail_content, 'html.parser')

    # mail_content not html
    is_mail_html = bool(soup.find())
    if not is_mail_html:
        return mail_content

    if mail_client == 'outlook':
        return trim_outlook(soup, mail_client)
    elif mail_client == 'mailspring':
        return trim_mailspring(soup)

    return mail_content


def trim_mailspring(soup):
    # trim thread
    gmail_quote_attribution_div = soup.findChild(
        'div', {'class': 'gmail_quote_attribution'},
        recursive=False)

    if gmail_quote_attribution_div:
        extra_tags = gmail_quote_attribution_div.find_next_siblings()
        for tag in extra_tags:
            tag.decompose()

        gmail_quote_attribution_div.decompose()

    # trim signature
    signature = soup.findChild(
        lambda p:
        p.findChild('signature', recursive=False),
        recursive=False)

    if signature:
        signature.decompose()

    return str(soup)


def trim_outlook(soup, mail_client: str):
    pass


if __name__ == '__main__':

    all_mail_text = []
    mail_client = 'mailspring'

    sample_mails_list = [mail_response['message_body'] for mail_response in gmail_mailspring.mail_responses]

    for sno, mail in enumerate(sample_mails_list):
        trimmed_mail = trim_the_mail(mail, mail_client)
        all_mail_text.append({"sno": sno, "message_body": trimmed_mail})

    with open('output.json', 'w') as f:
        json.dump(all_mail_text, f)
