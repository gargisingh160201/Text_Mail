def trim_the_mail(text):
    # assumption: target string will always be there.
    target_strings = ['On Mon', 'On Tue', 'On Wed', 'On Thu', 'On Fri', 'On Sat', 'On Sun']


    for target in target_strings:
        target_index = text.rfind(target)
        if target_index >= 0:
            break
    else:
        return text

    text = text[:target_index]

    return text



if  __name__=="__main__":
    mail= "Gargi On Hello vacation noMnO On On Mon, Mar 11, 2021 at 2:04 PM Ashish Jharkhande <tcs_indore@hellomailtest.msg91.com> wrote: Your ticket id is #537 please use this for reference   The views and opinions included in this email belong to their author and do not necessarily mirror the views and opinions of the company. Our employees are obliged not to make any defamatory clauses, infringe, or authorize infringement of any legal right. Therefore, the company will not take any liability for such statements included in emails. In case of any damages or other liabilities arising, employees are fully responsible for the content of their emails. "

    # input_mail=mail.replace(" ","")
    print(trim_the_mail(mail))

