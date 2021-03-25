from sample_test_cases import mailspring, outlook, yahoo, gmail
from bs4 import BeautifulSoup
import json
import logging
from custom_exceptions import *
import os
import re

logger = logging.getLogger(__name__)


def trim_the_mail(mail_content, mail_client):
    allowed_mail_clients = [
        'mailspring',
        'outlook',
        'gmail',
        'yahoo'
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
        elif mail_client == 'gmail':
            return trim_gmail(soup)
        elif mail_client == 'yahoo':
            return trim_yahoo(soup)

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


def trim_gmail(soup):
    try:
        first_div = soup.find('div', {"dir": "ltr"})

        signature = first_div.find('div', {"dir": "ltr", "class": "gmail_signature"}, recursive=False)
        if signature:
            signature.decompose()

        gmail_quote_div = soup.find('div', {'class': 'gmail_quote'})
        if gmail_quote_div:
            gmail_attr_div = gmail_quote_div.find('div', {'dir': 'ltr', 'class': 'gmail_attr'})
            if '---------- Forwarded message ---------' not in gmail_attr_div.getText():
                gmail_quote_div.decompose()

        for div in soup.find_all("div", {'class': 'gmail_signature'}):
            div.decompose()

        # div_siblings = [first_div] + (first_div.find_next_siblings('div'))

        return str(first_div)

    except Exception as e:
        logger.exception(e)
        print(e)


def trim_yahoo(soup):
    # para_tag = soup.find('div', {"class": "yahoo-style-wrap"})
    #
    # if para_tag:
    #     required_text = para_tag.find_all('div', {"dir": "ltr"})
    #     return str(required_text)
    #
    # for EachPart in soup.select('div[class*="yahoo-style-wrap"]'):
    #     return str(EachPart)
    #
    # signature_tag = soup.select('div[class*="signature"]')
    # if signature_tag:
    #     signature_tag[0].decompose()
    #
    # first_div = soup.find('div', {"dir": "ltr"})
    #
    # if first_div is None:
    #     for EachPart in soup.select('div[class*="yahoo_quoted"]'):
    #         return str(EachPart)
    # else:
    #     return str(first_div)

    yahoo_quoted_div = soup.body.find('div', {'class': 'yahoo_quoted'}, recursive=False)
    if yahoo_quoted_div:
        yahoo_quoted_div.decompose()
    yahoo_style_wrap=soup.body.find('div', {'class': re.compile('.*yahoo-style-wrap')})
    if yahoo_style_wrap:
        signature_tag=yahoo_style_wrap.find('div', {'class': re.compile('.*signature')})
        if signature_tag:
            signature_tag.decompose()

    return str(soup)




if __name__ == '__main__':

    try:
        all_mail_text = []
        mail_client = 'yahoo'

        sample_mails_list = [
            mail_response['message_body']
            for mail_response in yahoo.mail_responses
        ]

        for sno, mail in enumerate(sample_mails_list):
            trimmed_mail = trim_the_mail(mail, mail_client)
            all_mail_text.append({"sno": sno, "message_body": trimmed_mail})

        with open(os.path.join('outputs', f'output_{mail_client}.json'), 'w') as f:
            json.dump(all_mail_text, f)

    except Exception as e:
        logger.exception('Something went wrong in main method')
        print(e)
