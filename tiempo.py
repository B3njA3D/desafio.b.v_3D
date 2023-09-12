def segundo_a_minutos(segundos):
    return segundos /60

def minutos_a_horas(minutos):
    return minutos /60

if __name__=="__main__":
    segundos = 150
    minutos= segundo_a_minutos(segundos)
    print(f"{segundos} segundos son equivalentes a {minutos} minutos")