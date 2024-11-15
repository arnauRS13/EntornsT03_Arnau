from ciutats import ciutats
code=int(input("introdueix code postal"))
t = None
for ciutat,dade in ciutats.items():
    if dade['code_postal'] == code:
        t = ciutat
if t :
    print(f"aquest code de postal {code} de ciutat {t}")
else:
    print(f"no s'ha trobat ciutat de aquest code postal {code}")

