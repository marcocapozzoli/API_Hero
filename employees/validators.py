from validate_docbr import CNPJ

def validate_cnpj(value):
    cnpj = CNPJ()
    return cnpj.validate(value)
