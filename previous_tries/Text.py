def trim_the_mail(my):
    extra = my[::-1]
    if extra.find('uhTnO')!=-1:
        end_ind = extra.find('uhTnO')
        final_string = extra[end_ind + 5:]
        final=final_string[::-1]
        for i in range(len(mail)):
            if mail[i] == " ":
                ind.append(i)
        y = list(final)
        new = []
        for i in ind:
            y.insert(i, " ")
        t = []
        for i in range(len(y)):
            if i < (len(y) - 1) and y[i] == " " and y[i + 1] == " ":
                break
            elif i < (len(y) - 1):
                t.append(y[i])
        s = " "
        for i in t:
            if i == " ":
                s = s + i
            else:
                s = s + i
        return s
    elif extra.find('noMnO')!=-1:
        end_ind = extra.find('noMnO')
        end_ind=end_ind + 5
        ind=[]
        final_string = extra[end_ind :]
        final=final_string[::-1]
        for i in range(len(mail)):
            if mail[i] == " ":
                ind.append(i)
        y = list(final)
        new = []
        for i in ind:
            y.insert(i, " ")
        t = []
        for i in range(len(y)):
            if i < (len(y) - 1) and y[i] == " " and y[i + 1] == " ":
                break
            elif i < (len(y) - 1):
                t.append(y[i])
        s = " "
        for i in t:
            if i == " ":
                s = s + i
            else:
                s = s + i
        return s
    elif extra.find('euTnO')!=-1:
        end_ind = extra.find('euTnO')
        final_string = extra[end_ind + 5:]
        final=final_string[::-1]
        for i in range(len(mail)):
            if mail[i] == " ":
                ind.append(i)
        y = list(final)
        new = []
        for i in ind:
            y.insert(i, " ")
        t = []
        for i in range(len(y)):
            if i < (len(y) - 1) and y[i] == " " and y[i + 1] == " ":
                break
            elif i < (len(y) - 1):
                t.append(y[i])
        s = " "
        for i in t:
            if i == " ":
                s = s + i
            else:
                s = s + i
        return s
    elif extra.find('deWnO')!=-1:
        end_ind = extra.find('deWnO')
        final_string = extra[end_ind + 5:]
        final=final_string[::-1]
        for i in range(len(mail)):
            if mail[i] == " ":
                ind.append(i)
        y = list(final)
        new = []
        for i in ind:
            y.insert(i, " ")
        t = []
        for i in range(len(y)):
            if i < (len(y) - 1) and y[i] == " " and y[i + 1] == " ":
                break
            elif i < (len(y) - 1):
                t.append(y[i])
        s = " "
        for i in t:
            if i == " ":
                s = s + i
            else:
                s = s + i
        return s
    elif extra.find('irFnO')!=-1:
        end_ind = extra.find('irFnO')
        final_string = extra[end_ind + 5:]
        final=final_string[::-1]
        for i in range(len(mail)):
            if mail[i] == " ":
                ind.append(i)
        y = list(final)
        new = []
        for i in ind:
            y.insert(i, " ")
        t = []
        for i in range(len(y)):
            if i < (len(y) - 1) and y[i] == " " and y[i + 1] == " ":
                break
            elif i < (len(y) - 1):
                t.append(y[i])
        s = " "
        for i in t:
            if i == " ":
                s = s + i
            else:
                s = s + i
        return s
   
    elif extra.find('taSnO')!=-1:
        end_ind = extra.find('taSnO')
        final_string = extra[end_ind + 5:]
        final=final_string[::-1]
        for i in range(len(mail)):
            if mail[i] == " ":
                ind.append(i)
        y = list(final)
        new = []
        for i in ind:
            y.insert(i, " ")
        t = []
        for i in range(len(y)):
            if i < (len(y) - 1) and y[i] == " " and y[i + 1] == " ":
                break
            elif i < (len(y) - 1):
                t.append(y[i])
        s = " "
        for i in t:
            if i == " ":
                s = s + i
            else:
                s = s + i
        return s
    elif extra.find('nuSnO')!=-1:
        end_ind = extra.find('nuSnO')
        final_string = extra[end_ind + 5:]
        final=final_string[::-1]
        for i in range(len(mail)):
            if mail[i] == " ":
                ind.append(i)
        y = list(final)
        new = []
        for i in ind:
            y.insert(i, " ")
        t = []
        for i in range(len(y)):
            if i < (len(y) - 1) and y[i] == " " and y[i + 1] == " ":
                break
            elif i < (len(y) - 1):
                t.append(y[i])
        s = " "
        for i in t:
            if i == " ":
                s = s + i
            else:
                s = s + i
        return s

if  __name__=="__main__":
    mail= "Gargi On Hello vacation noMnO On On Mon, Mar 11, 2021 at 2:04 PM Ashish Jharkhande <tcs_indore@hellomailtest.msg91.com> wrote: Your ticket id is #537 please use this for reference   The views and opinions included in this email belong to their author and do not necessarily mirror the views and opinions of the company. Our employees are obliged not to make any defamatory clauses, infringe, or authorize infringement of any legal right. Therefore, the company will not take any liability for such statements included in emails. In case of any damages or other liabilities arising, employees are fully responsible for the content of their emails. "

    input_mail=mail.replace(" ","")
    print(trim_the_mail(input_mail))

