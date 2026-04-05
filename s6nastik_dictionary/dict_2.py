"""Tõlgi (väljasta ekraanile) järgmised sõnad:

tere -> inglise k, itaalia k
auto -> itaalia k
kass - > inglise k
üks -> itaalia k
kolm -> inglise k"""

from dict import est_eng_dict, est_it_dict
est_it_dict["üks"] = "uno"
est_it_dict["kolm"] = "tre"
est_eng_dict["üks"] = "one"
est_eng_dict["kolm"] = "three"

print(f"Tere -> inglise keeles: {est_eng_dict["tere"]}, itaalia keeles: {est_it_dict["tere"]}")
print(f"Auto on itaalia keeles {est_it_dict["auto"]}")
print(f"Kass inglise keeles on {est_eng_dict["kass"]}")
print(f"Üks itaalia keeles on {est_it_dict["üks"]}")
print(f"Kolm inglise keeles on {est_eng_dict["kolm"]}")


