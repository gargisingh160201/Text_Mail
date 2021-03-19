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

    # approach1
    # root_elements = soup.findChildren()
    #
    # for i, element in enumerate(root_elements):
    #     element_class = element.attrs.get('class')
    #     if element_class and 'gmail_quote_attribution' in element_class:
    #         gmail_quote_attribution_index = i
    #         break
    # else:
    #     return ''.join([str(e) for e in root_elements])
    #
    # relevant_elements = root_elements[:gmail_quote_attribution_index]
    #
    # return ''.join([str(e) for e in relevant_elements])

    # approach2

    gmail_quote_attribution_div = soup.find('div', {'class': 'gmail_quote_attribution'})

    # remove threads
    if gmail_quote_attribution_div:
        extra_tags = [gmail_quote_attribution_div] + gmail_quote_attribution_div.find_next_siblings()

        for tag in extra_tags:
            tag.decompose()

    # remove signatures
    signature_tags = soup.find_all('signature')
    if signature_tags:
        for tag in signature_tags:
            tag.decompose()

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
