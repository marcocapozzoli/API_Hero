from validate_docbr import CPF

def validate_cpf(value):
    cpf = CPF()
    return cpf.validate(value)
