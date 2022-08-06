# public variable is the variable which is publically available
# protected variable is the variable which is only available for my family
# private variable is the variable which is available for me ONLY


class employee:
    pub=50      # public variable
    _prot=100   #protected variable
    __priv=150  #private variable

emp= employee()
print(emp.pub)
print(emp._prot)
print(emp._employee__priv)