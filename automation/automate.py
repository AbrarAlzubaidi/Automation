import re

def find_emails():
    lines = []
    emails=[]
    email_list=''
    with open('assest/potentialContacts.txt',"r") as f1:
        content=f1.readlines()
        for itemLine in content:
            if "@" in itemLine:
                item =str(itemLine)    
                lines.append(item.split())
        
        for i in lines:
            for j in i:
                if "@" in j:
                    emails.append(j)
        emails.sort()
        email_list="\n".join(emails)

    with open ('assest/email_list.txt',"w") as f2:
        f2.write(email_list)

"""
(xxx) yyy-zzzz, yyy-zzzz, xxx-yyy-zzzz, etc.
phone numbers with missing area code should presume 206
phone numbers should be stored in xxx-yyy-zzzz format.
"""
def find_numbers():
    lines=[]
    phones=[]
    with open('assest/potentialContacts.txt',"r") as f1:
        content=f1.readlines()
        for itemLine in content:
            item =str(itemLine)
            lines.append(item.split('.'))
        
        for i in lines:
            for j in i:
                if re.match('[0-9][^A-Z]*', j):
                    phones.append(j)
    string = "".join(phones)
   
    q=re.findall('[0-9][^A-Z]*', string)

    with open ('assest/phone_list.txt',"w") as f2:
        f2.write('\n'.join(q))


find_emails()
find_numbers()
# 555-555 5555
if __name__ == '__main__':
    # regex=r'/^(\(\d{3}\)|\d{3})(\s?|-)(\d{3})(\s?|-?)(\d{4})$/g'
    if re.match('/^(\(\d{3}\)|\d{3})(\s?|-)(\d{3})(\s?|-)(\d{4})$/g','555-555-5555'):
        print('yes')
    else:
        print('no')
    # pattern = re.compile('/^(\(\d{3}\)|\d{3})(\s?|-)(\d{3})(\s?|-)(\d{4})$/g')
    # x=pattern.match('555-555 5555')
    # print(x)
