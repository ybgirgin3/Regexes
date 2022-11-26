# Regexes

Easy regex finder for Python

## installation
```sh
~$ pip install Regexes
```

Usage:

- For extracting all possible info from string

```py
from Regexes import Regexes


string = """
Hello My name is Berkay and this is my project
bekxxx3@gmail.com, beskilo@doner.com,
05323450002,
05430000778,
pythoncibeko@bekocanholding.com
"""

ret = Regexes(data=string).find_reg()
print(ret)


# ---------------------------
# {'btc_addresses': [],
#  'credit_cards': [],
#  'dates': [],
#  'emails': ['bekxxx3@gmail.com',
#             'beskilo@doner.com',
#             'pythoncibeko@bekocanholding.com'],
#  'hex_colors': [],
#  'ips': [],
#  'ipv6s': [],
#  'links': ['gmail.com', 'doner.com', 'bekocanholding.com'],
#  'phones': ['05323450002', '05430000778'],
#  'phones_with_exts': [],
#  'po_boxes': [],
#  'prices': [],
#  'ssn_number': [],
#  'street_addresses': [],
#  'times': [],
#  'zip_codes': []}

```

- For specific type of info

```py
from Regexes import Regexes


string = """
Hello My name is Berkay and this is my project
bekxxx3@gmail.com, beskilo@doner.com,
05323450002,
05430000778,
pythoncibeko@bekocanholding.com
"""

ret = Regexes(data=string, dtype="emails").find_reg() # * Just add dtype arg
print(ret)


# ---------------------------
# {'emails': ['bekxxx3@gmail.com',
#             'beskilo@doner.com',
#             'pythoncibeko@bekocanholding.com']}

```

Credit: [CommonRegex](https://github.com/madisonmay/CommonRegex)
