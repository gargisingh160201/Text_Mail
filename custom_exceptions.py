class NotFoundError(Exception):
    def __init__(self, message='Some parameter missing'):
        self.message = message
        # self.mail_content = mail_content
        # self.mail_client = mail_client

    # def __str__(self):
    #     return f'{self.message}. You provided mail_content: {self.mail_content} and mail_client: {self.mail_client}'

class NotAllowedError(Exception):
    def __init__(self, message='This param is not allowed'):
        self.message = message
        # self.mail_content = mail_content
        # self.mail_client = mail_client

    # def __str__(self):
    #     return f'{self.message}. You provided mail_content: {self.mail_content} and mail_client: {self.mail_client}'