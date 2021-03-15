import unittest
import Text
import Text2

class mails(unittest.TestCase):

    def test_clear(self):
        f1 = "hello on giant noMnO On Mon, Mar 11, 2021 at 2:04 PM Ashish Jharkhande <tcs_indore@hellomailtest.msg91.com> wrote: Your ticket id is #537 please use this for reference   The views and opinions included in this email belong to their author and do not necessarily mirror the views and opinions of the company. Our employees are obliged not to make any defamatory clauses, infringe, or authorize infringement of any legal right. Therefore, the company will not take any liability for such statements included in emails. In case of any damages or other liabilities arising, employees are fully responsible for the content of their emails."
        f1=f1.replace(" ","")
        f2= "hello on giant noMnO "
        f2=f2.replace(" ","")
        self.assertEqual(Text.trim_the_mail(f1),f2)

    def test_clear2(self):
        f1 = "hello on giant noMnO no On Tue, Mar 11, 2021 at 2:04 PM Ashish Jharkhande <tcs_indore@hellomailtest.msg91.com> wrote: Your ticket id is #537 please use this for reference   The views and opinions included in this email belong to their author and do not necessarily mirror the views and opinions of the company. Our employees are obliged not to make any defamatory clauses, infringe, or authorize infringement of any legal right. Therefore, the company will not take any liability for such statements included in emails. In case of any damages or other liabilities arising, employees are fully responsible for the content of their emails."

        f2 = "hello on giant noMnO no "

        self.assertEqual(Text2.trim_the_mail(f1),f2)