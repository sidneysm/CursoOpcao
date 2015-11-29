from enum import Enum

class Situacao(Enum):
	confir = "Pagamento Confirmado"
	aguardando = "Aguardando confirmação do pagamento"
	nao_pago = "Pagamento não efetuado"