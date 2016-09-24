#!/usr/python3.5
# o modulo bge e importado automaticamente
# blender -P blender_c.py
# exemplo (modulo para teleport)

# obtem o dono do controlador
controlador = bge.logic.getCurrentController()
dono = controlador.owner

# obtem a cena
cena = bge.logic.getCurrentScene()

# objtem o destino
destino = cena.objeto['Portal']

# obtem as cooredenadas do destino
x, y, z = destino.position

# move o personagem para 1 BU acima do destino
dono.position = [x, y, z+1]
