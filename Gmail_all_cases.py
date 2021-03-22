from sample_test_cases import Gmail
from bs4 import BeautifulSoup
from sample_test_cases import Gmail
import json
def trim_the_mail(mail_text: str, mail_client: str):



    soup = BeautifulSoup(mail_text, 'lxml')
    is_html = bool(soup.find())
    if not is_html: # exception
        return mail_text
    if mail_client == 'gmail':
        return trim_gmail(soup)

    return mail_text
def trim_gmail(soup):



    first_div = soup.find('div',{"dir": "ltr"})

    for div in soup.find_all("div", {'class': 'gmail_signature'}):
        div.decompose()


    # div_siblings = [first_div] + (first_div.find_next_siblings('div'))



    return str(first_div)

if __name__ == '__main__':
    all_mail_text = []
    mail_client = 'gmail'

    sample_mails_list = [response['message_body'] for response in Gmail.Responses]

    for sno, mail in enumerate(sample_mails_list):
        trimmed_mail = trim_the_mail(mail, mail_client)
        all_mail_text.append({"sno": sno, "message_body": trimmed_mail})

    with open('output.json', 'w') as f:
        json.dump(all_mail_text, f)