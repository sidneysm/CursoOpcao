#/usr/bin/env python
# -*- coding:UTF-8 -*-
# fonte: http://www.python.org.br/wiki/VerificadorDeCPF
from decimal import *
import pyboleto
from pyboleto.bank.bancodobrasil import BoletoBB
from pyboleto.data import BoletoData
from pyboleto.pdf import BoletoPDF
from pyboleto.html import BoletoHTML
from .models import *

import datetime

import re

try:
    unicode = unicode
except NameError:
    # 'unicode' is undefined, must be Python 3
    str = str
    unicode = str
    bytes = bytes
    basestring = (str,bytes)
else:
    # 'unicode' exists, must be Python 2
    str = str
    unicode = unicode
    bytes = str
    basestring = basestring

try:
    xrange
except NameError:
    xrange = range



# traduz 123.456.789-10 para 12345678910
_translate = lambda cpf: ''.join(re.findall("\d", cpf))

def _exceptions(cpf):
    """Se o número de CPF estiver dentro das exceções é inválido

    """
    if len(cpf)!=11:
        return True
    else:
        s=''.join(str(x) for x in cpf)
        if s=='00000000000' or s=='11111111111' or s=='22222222222' or s=='33333333333' or s=='44444444444' or s=='55555555555' or s=='66666666666' or s=='77777777777' or s=='88888888888' or s=='99999999999':
            return True
    return False

def _gen(cpf):
    """Gera o próximo dígito do número de CPF

    """
    res = []
    for i, a in enumerate(cpf):
        b = len(cpf) + 1 - i
        res.append(b * a)

    res = sum(res) % 11

    if res > 1:
        return 11 - res
    else:
        return 0


class CPF(object):

    _gen = staticmethod(_gen)
    _translate = staticmethod(_translate)
    
    def __init__(self, cpf):
        """O argumento cpf pode ser uma string nas formas:

        12345678910
        123.456.789-10

        ou uma lista ou tuple
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 0]
        (1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 0)

        """
        
        if isinstance(cpf, basestring):
            if not cpf.isdigit():
               cpf = self._translate(cpf)
            
        self.cpf = [int(x) for x in cpf]

    def __getitem__(self, index):
        """Retorna o dígito em index como string

        """
        
        return self.cpf[index]

    def __repr__(self):
        """Retorna uma representação 'real', ou seja:

        eval(repr(cpf)) == cpf
        
        """
        
        return "CPF('%s')" % ''.join(str(x) for x in self.cpf)

    def __eq__(self, other):
        """Provê teste de igualdade para números de CPF

        """

        return isinstance(other, CPF) and self.cpf == other.cpf
    
    def __str__(self):
        """Retorna uma representação do CPF na forma:

        123.456.789-10

        """

        d = iter("..-")
        s = [str(x) for x in self.cpf]
        for i in xrange(3, 12, 4):
            s.insert(i, next(d))
        r = ''.join(s)
        return r

    def isValid(self):
        """Valida o número de cpf

        """
        
        if _exceptions(self.cpf):
            return False

        s = self.cpf[:9]
        s.append(self._gen(s))
        s.append(self._gen(s))
        return s == self.cpf[:]

# VALIDO = "113.451.253-80"
# INVALIDO = "31354110274"

# # qualquer um dos dois formatos (com pontos ou não) pode ser usado

# valido = CPF(VALIDO)
# invalido = CPF(INVALIDO)

# print (valido.isValid())

def print_bb(Aluno):
    listaDados = []
    for i in range(1):
        d = BoletoBB(7, 2)

        d.nosso_numero          = '%d' % (i + 1)
        d.numero_documento      = '123456789'
        d.convenio              = '7777777'
        d.especie_documento     = 'DM'

        d.carteira              = '18'
        d.cedente               = 'Curso Opção Triunfo'
        d.cedente_documento     = "05261501490"
        d.cedente_endereco      = "Rua Alameda das Mansões"
        d.agencia_cedente       = '2739'
        d.conta_cedente         = '12097'

        d.data_vencimento       = datetime.date(2015, 12, 21)
        d.data_documento        = datetime.date(2015, 12, 20)
        d.data_processamento    = datetime.date(2015, 12, 20)

        d.instrucoes            = [
        "- Sr Caixa, cobrar multa de 2% após vencimento",
        "- Receber até 10 dias após vencimento",
        ]
        d.demonstrativo         = [
        "- Testando pagamento",
        "- Total R$ 5,00",
        ]
        d.valor_documento       = Decimal(600)



        d.sacado_nome           =  Aluno.first_name
        d.sacado_documento      = '06072300456' 
        d.sacado_cidade         = Aluno.endereco
        d.sacado_uf             = 'RN'
        d.sacado_endereco       = 'Rua rua'
        d.sacado_bairro         = 'Sao Pedro'
        d.sacado_cep            = '3333333'



        d.valor                 = Decimal(600)
        d.valor_documento       = Decimal(600)

        d.quantidade            =   '1'

        d.barcode


        listaDados.append(d)

        boleto = BoletoPDF('curso/boletos/boleto-teste-%s.pdf' % d.sacado_nome )
        
        for i in listaDados:
            boleto.drawBoleto(i)
            boleto.nextPage()
            boleto.save()
            



def print_all(Aluno):
    print ("Pyboleto version: %s" % pyboleto.__version__)
    print ("----------------------------------")
    print (" Printing Example Boletos ")
    print ("----------------------------------")

    print ("Banco do Brasil")
    print_bb()

    
if __name__ == "__main__":
    print_all()