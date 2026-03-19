from generator import vytvor_fakturu

class Klient:
	def __init__(self,meno,email,suma):
		self.meno = meno
		self.email = email
		self.suma = suma
	def __str__(self):
		return f"{self.meno}, {self.email}, {self.suma}"
	def vytvor_fakturu(self):
		vytvor_fakturu(self.meno, self.email, self.suma)


class VIPKlient(Klient):
	def __init__(self, meno, email, suma, zlava):
		super().__init__(meno, email, suma)
		self.zlava = zlava
	def vypocitaj_sumu(self):
		suma_po_zlave = self.suma * (1 - self.zlava / 100)
		return suma_po_zlave
	def info(self):
		print(f"{self.meno}, {self.email}, {self.suma}, zľava: {self.zlava}%, po zľave: {self.vypocitaj_sumu()}")
	

