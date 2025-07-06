vlan=int(input("Indique numero de vlan "))
if 1 <= vlan <=1005:
    print ("La Vlan es de rango normal. ") 
elif 1006 <= vlan <=4094:
    print ("La Vlan es de rango extendido. ")
else:
    print ("No es un numero valido. ") 
