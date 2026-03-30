"""Loo juurde kaks uut sõnastiku (e_inglise, e_itaalia), mille võti ei ole mitte eesti
keeles, vaid vastavalt kas inglise või itaalia keeles. Lisa sõnastikku ka kõik eelmises
sõnastikus olevad sõnad."""

from dict_2 import est_eng_dict, est_it_dict

eng_est_dict = {"car": "auto", "dog": "koer", "cat": "kass", "hello": "tere", "one": "üks", "three": "kolm"}
it_est_dict = {"auto": "auto", "cane": "koer", "catta": "kass", "ciao": "tere", "uno": "üks", "tre": "kolm"}

est_eng_dict["headaega"] = "goodbye"
est_eng_dict["pott"] = "pot"
est_eng_dict["sõnastik"] = "dictionary"
est_it_dict["headaega"] = "arrivederci"
est_it_dict["pott"] = "pentola"
est_it_dict["sõnastik"] = "dizionario"
eng_est_dict["goodbye"] = "headaega"
eng_est_dict["pot"] = "pott"
eng_est_dict["dictionary"] = "sõnastik"
it_est_dict["arrivederci"] = "headaega"
it_est_dict["pentola"] = "pott"
it_est_dict["dizionario"] = "sõnastik"
"""
Lisa kõikidesse sõnastikesse järgmised sõnad:

headaega - goodbye - arrivederci
pott - pot - pentola
sõnastik - dictionary - dizionario
Tõlgi (väljastage ekraanile) järgmised sõnad:

üks -> itaalia
ciao - > eesti
dog -> itaalia
pentola - inglise"""



print(f"Üks itaalia keeles on {est_it_dict["üks"]}")
print(f"Ciao eesti keeles on {it_est_dict["ciao"]}")
print(f"Dog in italian is {est_it_dict[eng_est_dict["dog"]]}")
print(f"Pentola in english is {est_eng_dict[it_est_dict["pentola"]]}")