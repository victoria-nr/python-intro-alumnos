
#Calcular lo que se ha pagado durante 10 meses, si comienzas de 10€ y si cada mes se dobla la cantidad a pagar
pago_acum = 0  
pago = 10      

for mes in range(1, 11):  
    pago_acum += pago    
    print(f'En el mes {mes} pagó {pago} €')
    pago *= 2       

print("Al final de los 20 meses tuvo que pagar:", pago_acum)
