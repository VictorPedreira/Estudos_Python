"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condilões no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade  = 61 # velocidade atual do carro
local_carro = 100 # local em que o carro está na estrada

RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar pega

vel_carro_pass_radar_1 = velocidade > RADAR_1
range_radar_1 = LOCAL_1 - RADAR_RANGE
range_radar_2 = LOCAL_1 + RADAR_RANGE
carro_passou_radar = local_carro >= range_radar_1 and local_carro <= range_radar_2
carro_multado_radar = carro_passou_radar and vel_carro_pass_radar_1

if vel_carro_pass_radar_1:
    print("Velocidade do carro passou do radar 1")

if carro_passou_radar:
    print("Carro passou do radar 1")

if carro_multado_radar:
    print("Carro multado em radar 1")    