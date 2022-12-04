from Regexes import Regexes
from pprint import pprint


string = """
Hello My name is Berkay and this is my project 
bekxxx3@gmail.com, beskilo@doner.com,
05323450002,
05430000778,
pythoncibeko@bekocanholding.com
"""

ret = Regexes(data=string, dtype="phones").find_reg()
pprint(ret)

# match = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', string)
# regex = re.compile(r'[\w.+-]+@[\w-]+\.[\w.-]+')
# match = re.findall(regex, string)
# print(match)
