"""Elabora un algoritmo que muestre la factura de la siguiente compra: 
El señor Pedro Ramirez compró en Falabella dos jeans de $125mil c/u, 2 camisas de $45mil c/u, 1 camiseta tipo polo por $30mil.
Tener en cuenta lo siguiente: *Si la compra lleva camisa tipo polo tiene un descuento del 5%, " 
                              *si es superior a $200mil del 30%
-Mostrar el total a pagar y el total de descuento (ahorro) del cliente en la compra"""


jeans= (2*125000)
camisas=(2*45000)
camiseta_polo= 30000
subtotal_compra = int(jeans + camisas + camiseta_polo)
camisa_polo=True

if camisa_polo == True:
    descuento_camisa_polo = (5/100)*camiseta_polo
else:
    descuento_camisa_polo = 0

if subtotal_compra > 200000:
    descuento_compra= 0.3*subtotal_compra
    total_compra= (subtotal_compra - descuento_camisa_polo)
    
else:
    descuento_compra = 0
    total_compra= subtotal_compra

print ("Cliente: Pedro Ramirez,\nArtículos:\n 2 Jeans: 125000 c/u\n 2 Camisas: 45000 c/u\n1 Camiseta Polo: 30000\n ({Subtotal_compra}Descuentos:{descuento_camisa_polo} {descuento_compra}{total_compra}")