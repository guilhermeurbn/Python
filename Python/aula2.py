velocidade = 61
local_carro = 98

RADAR_1 = 60
LOCAL_RADAR = 100
RADAR_RANGE = 1 # a distancia que o radar pega +/- '1km'

diferenca_mais = local_carro + RADAR_RANGE
diferenca_menos = local_carro - RADAR_RANGE

if velocidade > RADAR_1:
    print("seu carro esta acima da velocidade permitido")
    if local_carro >= diferenca_menos and local_carro <= diferenca_mais:
        print("o radar te apamanhou no local aonde o carro se localizava")
