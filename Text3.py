from sample_test_cases import sample_mail_bodies
from bs4 import BeautifulSoup

def mail_thread_to_text(mail_txt: str):

    if not mail_txt:
        return mail_txt

    soup = BeautifulSoup(mail_txt, 'lxml')
    is_html = bool(soup.find())
    if not is_html:
        return mail_txt

    first_ltr = soup.find('div')

    return first_ltr.text if first_ltr else mail_txt

if __name__ == '__main__':
    pure_text = mail_thread_to_text(sample_mail_bodies[0].get('message_body'))
    # print(pure_text)

    all_mail_text = []

    sample_mails = [mail['message_body'] for mail in sample_mail_bodies]
    for mail in sample_mails:
        all_mail_text.append(mail_thread_to_text(mail))

    print(all_mail_text)