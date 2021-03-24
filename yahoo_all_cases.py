from sample_test_cases import yahoo
from bs4 import BeautifulSoup
import json
import logging

logger = logging.getLogger(__name__)


def trim_the_mail(mail_text: str, mail_client: str):
    soup = BeautifulSoup(mail_text, 'lxml')
    is_html = bool(soup.find())
    if not is_html:
        return mail_text
    if mail_client == 'yahoo':
        return trim_yahoo(soup)

    return mail_text




def trim_yahoo(soup):
    para_tag=soup.find('div',{"class":"yahoo-style-wrap"})
    if para_tag:
        required_text=para_tag.find_all('div',{"dir":"ltr"})
        return str(required_text)
    for EachPart in soup.select('div[class*="yahoo-style-wrap"]'):
               return str(EachPart)
    signature_tag=soup.select('div[class*="signature"]')
    signature_tag.decompose()

    first_div = soup.find('div',{"dir": "ltr"})

    if first_div is None:
        for EachPart in soup.select('div[class*="yahoo_quoted"]'):
               return str(EachPart)
    else:
            return str(first_div)

if __name__ == '__main__':
    # pure_text = mail_thread_to_text(sample_mail_bodies[-2].get('message_body'))
    # print(pure_text)

    try:
        all_mail_text = []
        mail_client = 'yahoo'

        sample_mails_list = [response['message_body'] for response in yahoo.Responses]

        for sno, mail in enumerate(sample_mails_list):
            trimmed_mail = trim_the_mail(mail, mail_client)
            all_mail_text.append({"sno": sno, "message_body": trimmed_mail})

        with open('output_yahoo.json', 'w') as f:
            json.dump(all_mail_text, f)
    except FileNotFoundError as e:
        logger.exception('Error while dumping file')
        print(e)
