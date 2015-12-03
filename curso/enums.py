from enum import Enum

class Situacao(Enum):
	"""
	Define as possiveis situações de estado do pagamento.
	"""
	pago = "Pagamento Confirmado"
	aguardando = "Aguardando confirmação do pagamento"
	nao_pago = "Pagamento não efetuado"