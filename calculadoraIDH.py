
"""
Created on Mon Apr 15 19:59:03 2024

@author: casa
"""

indice_esperanza_de_vida = float(input("Ingresa el indice de esperanza de vida del pais : "))
indice_inbpc = float(input("Ingresa el indice de ingreso nacional bruto per capita del pais: "))
indice_de_educacion = float(input("Ingresa el indice de educacion del pais: "))

idh = (indice_esperanza_de_vida*indice_inbpc*indice_de_educacion)**(1/3)

print("El IDH del pais es: ", idh)

if idh >= 0.8:
    print("El IDH del pais es alto.")
    
elif idh >= 0.5 and idh < 0.8:
    print("El IDH del pais es medio.")
    
else :
    print("El IDH del pais es bajo.")