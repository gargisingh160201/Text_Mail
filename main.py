from sample_test_cases import hotmail
from bs4 import BeautifulSoup

def mail_thread_to_text(mail_txt: str):

    if not mail_txt:
        return mail_txt

    soup = BeautifulSoup(mail_txt, 'lxml')
    is_html = bool(soup.find())
    if not is_html:
        return mail_txt

    first_div = soup.find(['div', 'p']) # p for thunderbird
    # div_siblings = [first_div] + (first_div.find_next_siblings('div'))

    # pure_text = ''
    #
    # is_thread = not (len(div_siblings) < 2)
    #
    # if is_thread:
    #     for div in div_siblings[:-1]:
    #         pure_text += '{}\n'.format(div.text)
    #     return pure_text
    #
    # return div_siblings[0].text

    return first_div.text

if __name__ == '__main__':
    # pure_text = mail_thread_to_text(sample_mail_bodies[-2].get('message_body'))
    # print(pure_text)

    all_mail_text = []

    sample_mails = [mail['message_body'] for mail in hotmail.mail_responses]
    for mail in sample_mails:
        all_mail_text.append(mail_thread_to_text(mail))

    print(all_mail_text)