from sample_test_cases import Gmail
from bs4 import BeautifulSoup
from sample_test_cases import Gmail
import json
import logging

logger = logging.getLogger(__name__)


def trim_the_mail(mail_text: str, mail_client: str):
    soup = BeautifulSoup(mail_text, 'lxml')
    is_html = bool(soup.find())
    if not is_html:
        return mail_text
    if mail_client == 'gmail':
        return trim_gmail(soup)

    return mail_text


def trim_gmail(soup):
    try:
        first_div = soup.find('div', {"dir": "ltr"})
        signature=first_div.find('div',{"dir":"ltr","class":"gmail_signature"},recursive=False)
        if signature:
            latest_mail=first_div.find('div',{"dir":"ltr"},recursive=False)
            return str(latest_mail)
        forward_and_reply=soup.find('div',{'dir':'gmail_quote'})
        if forward_and_reply:
          for div in forward_and_reply.find('div', {'dir':'ltr','class': 'gmail_attr'}):
            if '---------- Forwarded message ---------' not in div.getText():
                div.decompose()


        for div in soup.find_all("div", {'class': 'gmail_signature'}):
             div.decompose()


    # div_siblings = [first_div] + (first_div.find_next_siblings('div'))

        return str(first_div)
    except Exception as e:
        logger.exception(e)
        print(e)



if __name__ == '__main__':
    try:
        all_mail_text = []
        mail_client = 'gmail'

        sample_mails_list = [response['message_body'] for response in Gmail.Responses]

        for sno, mail in enumerate(sample_mails_list):
            trimmed_mail = trim_the_mail(mail, mail_client)
            all_mail_text.append({"sno": sno, "message_body": trimmed_mail})

        with open('output.json', 'w') as f:
            json.dump(all_mail_text, f)
    except FileNotFoundError as e:
        logger.exception('Error while dumping file')
        print(e)
