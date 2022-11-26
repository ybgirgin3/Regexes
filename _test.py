from regexes import Regexes


string = """
Hello My name is Berkay and this is my project 
bekxxx3@gmail.com, beskilo@doner.com,
05323450002,
05430000778,
pythoncibeko@bekocanholding.com
"""

ret = Regexes(data=string, dtype="emails").find_reg()
print(ret)

# match = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', string)
# regex = re.compile(r'[\w.+-]+@[\w-]+\.[\w.-]+')
# match = re.findall(regex, string)
# print(match)
