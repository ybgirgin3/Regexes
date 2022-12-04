# coding: utf-8
import re
from Regexes.utils import regexes
      

class Regexes:
    def __init__(self, data: str, dtype: str = "") -> None:
        self.data = data
        _dtypes = [k for k,v in regexes.items()]

        if len(dtype):
            assert dtype in _dtypes, \
                f"regex dtypes must be one of the {_dtypes}"
            self.dtypes = dtype 
        else:
            self.dtypes = _dtypes


    def find_reg(self):
        ret = {}

        if not isinstance(self.dtypes, list):
            self.dtypes = [self.dtypes]

        for reg in self.dtypes:
            ret[reg] = re.findall(regexes[reg], self.data)
        return ret

