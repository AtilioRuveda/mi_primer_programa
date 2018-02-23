queres_chocolate = (input("queres un chocolate? (si / no): "))
tenes_plata = (input("tenes plata para pagarlo? (si / no): "))
esta_eña = (input("esta eña para comprartelo? (si / no) :"))

if queres_chocolate == "si" and (tenes_plata == "si" or esta_eña == "si"):
    (print("bueno, compra"))
else:
    (print("ok, no hagas nada"))
