# Regexes

Regex Finder for Python

Easy regex finder for Python

Usage:

- For extracting all possible info from string

```py
from regexes import Regexes


string = """
Hello My name is Berkay and this is my project
bekxxx3@gmail.com, beskilo@doner.com,
05323450002,
05430000778,
pythoncibeko@bekocanholding.com
"""

ret = Regexes(data=string).find_reg()
print(ret)
```

- For specific type of info

```py
from regexes import Regexes


string = """
Hello My name is Berkay and this is my project
bekxxx3@gmail.com, beskilo@doner.com,
05323450002,
05430000778,
pythoncibeko@bekocanholding.com
"""

ret = Regexes(data=string, dtype="emails").find_reg() # * Just add dtype arg
print(ret)
```

Credit: [CommonRegex](https://github.com/madisonmay/CommonRegex)
