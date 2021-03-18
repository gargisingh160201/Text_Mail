from sample_test_cases import hotmail_outlook, gmail_mailspring
from bs4 import BeautifulSoup

def trim_the_mail(mail_content: str, mail_client: str):

    # mail_content
    if not mail_content:
        return mail_content

    soup = BeautifulSoup(mail_content, 'lxml')

    # mail_content not html
    is_mail_html = bool(soup.find())
    if not is_mail_html:
        return mail_content

    if mail_client == 'gmail':
        return trim_mailspring(soup, mail_client)
    elif mail_client == 'mailspring':
        return trim_mailspring(soup, mail_client)

    return mail_content

def trim_mailspring(soup, mail_client: str):
    root_elements = soup.body.findChildren()

    gmail_quote_attribution_index = -1
    for i, element in enumerate(root_elements):
        if element.attrs.get('class') == 'gmail_quote_attribution':
            gmail_quote_attribution_index = i
            break
    else:
        return soup.get_text(separator='\n', strip=True)

    relevant_elements = root_elements[:gmail_quote_attribution_index]

    pure_text = ""

    for element in relevant_elements:
        element += element.text or ''

    return pure_text


def trim_gmail(soup, mail_client: str):
    pass


if __name__ == '__main__':

    all_mail_text = []
    mail_client = 'mailspring'

    sample_mails_list = [mail_response['message_body'] for mail_response in gmail_mailspring.mail_responses]

    for mail in sample_mails_list:
        all_mail_text.append(trim_the_mail(mail, mail_client))

    print(all_mail_text)