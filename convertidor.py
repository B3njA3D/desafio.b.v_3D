import temperatura
import masa 
import tiempo

def convertir_temperatura(valor,unidad_origen, unidad_destino):
    if unidad_origen =="celsius" and unidad_destino == "fahrenheit":
        return temperatura.celsius_a_fahrenheit(valor)
    

def convertir_masa(valor, unidad_origen, unidad_destino):
    if unidad_origen =="kilogramos" and unidad_destino == "gramos":
        return masa.kilogramos_a_gramos(valor)
    

def convertir_tiempo(valor, unidad_origen, unidad_destino):
    if unidad_origen == "segundo" and unidad_destino == "minutos":
        return tiempo.segundo_a_minutos(valor)
    
if __name__== "__main__":
    valor=20
    unidad_origen= "celsius"
    unidad_destino= "fahrenheit"
    resultado= convertir_temperatura(valor,unidad_origen, unidad_destino)
    print(f"{valor}grados {unidad_origen} equivalen a {resultado} grados{unidad_destino}")