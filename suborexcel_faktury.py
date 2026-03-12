from generator import vytvor_fakturu
import pandas as pd 
import math

df = pd.read_excel("faktury.xlsx")

for index, riadok in df.iterrows():
	try:
		if math.isnan(riadok['suma']):
			raise ValueError("Chyba: suma je prázdna")
		vytvor_fakturu(riadok['meno'], riadok['email'], riadok['suma'])
		print(f"OK: {riadok['meno']}")
	except Exception as e:
		print(f"Chyba pri {riadok['meno']}: {e}.")
	