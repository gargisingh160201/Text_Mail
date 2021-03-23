from sample_test_cases import hotmail_outlook, gmail_mailspring
from bs4 import BeautifulSoup
import json
import logging
from exceptions import *

logger = logging.getLogger(__name__)



def trim_the_mail(mail_content, mail_client):
    allowed_mail_clients = [
        'mailspring',
        'outlook'
    ]

    try:
        if not mail_client:
            err_msg = "mail client cannot be empty"
            logger.exception(err_msg)
            raise NotFoundError(err_msg)

        if mail_client not in allowed_mail_clients:
            err_msg = f'this mail client is not allowed, we parse only {allowed_mail_clients}'
            logger.exception(err_msg)
            raise NotAllowedError(err_msg)

        if not mail_content:
            err_msg = 'mail content not provided'
            logger.exception(err_msg)
            raise NotFoundError(err_msg)


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

    except NotFoundError:
        raise
    except NotAllowedError:
        raise
    except Exception as E:
        logger.exception('Something went wrong.')
        print(E)


def trim_mailspring(soup):
    # trim thread
    # gets a div with class=gmail_quote_attribution in the root html
    try:
        thread_start_div = soup.findChild(
            'div', {'class': 'gmail_quote_attribution'},
            recursive=False)

        # if the mail is a thread, then remove thread and all elements below it
        if thread_start_div:
            extra_tags = thread_start_div.find_next_siblings()
            for tag in extra_tags:
                tag.decompose()

            thread_start_div.decompose()

        # trim signature
        # find the div which contains a signature element
        signature = soup.findChild(
            lambda p:
            p.findChild('signature', recursive=False),
            recursive=False)

        if signature:
            signature.decompose()

        return str(soup)
    except Exception as e:
        logger.exception(e)
        print(e)


def trim_outlook(soup, mail_client: str):
    pass


if __name__ == '__main__':

    try:
        all_mail_text = []
        mail_client = 'mailspring'

        sample_mails_list = [mail_response['message_body'] for mail_response in gmail_mailspring.mail_responses]

        for sno, mail in enumerate(sample_mails_list):
            trimmed_mail = trim_the_mail(mail, mail_client)
            all_mail_text.append({"sno": sno, "message_body": trimmed_mail})

        with open('output.json', 'w') as f:
            json.dump(all_mail_text, f)

    except FileNotFoundError as e:
        logger.exception('Something went wrong while writing ouput in file')
        print(e)
    except Exception as e:
        logger.exception('Something went wrong in main method')
        print(e)
