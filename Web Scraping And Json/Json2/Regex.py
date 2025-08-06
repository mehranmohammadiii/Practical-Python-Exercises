import re
str1='''
Conference1
Topic: Object Oriented Programming
Date: 09/20/2022
Location: USA
Web: conf.usa/09/2022
Cost: $1200
Conference2
Topic:    Python3
Date: 01/31/2022
Location: France
Web: conf.france/01/2022
Cost: $600
Conference3
Topic: Data Science
Date: 07/09/2022
Location: UK
Web: conf.org
Cost: $900
Conference4
Topic: Web Development
Date: 08/29/2022
Location: Canada
Web: conf.ca
Cost: $1
Conference5
Topic: Python for Beginners
Date: 05/09/2022
Location: Turkey
Web: conf.com/03/2022
Cost: $900000
'''
print(re.findall(r"Topic:\s*(.*)",str1))
print(re.findall(r"Date:\s*(\d{2}/\d{2}/\d{4})",str1))
print(re.findall(r"Date:\s*(\d{2})/\d{2}/\d{4}",str1))
print(re.findall(r"Topic:\s*(.+)\s.*\s.*\sWeb:\s*(conf.+2022)",str1))
print(re.findall(r"Cost:\s*(\$\d{2,4})\s",str1))
print(re.findall(r"Topic:\s*(.+)\s+Date:\s*09/\d{2}/\d{4}",str1))
print(re.sub(r"Cost:\s*\$(\d{2,4})\s","Cost: $555\n",str1))






