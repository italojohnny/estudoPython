#!/usr/python3.5
# blender -P blender_a.py
# exemplo de codigo para a criacao de uma cena com objeto
import bpy

# pega a cena inicia
cena = bpy.data.scenes[0]

# elementos da cena 'default'
camera = bpy.data.objects[0]
cubo = bpy.data.objects[1]
lamp = bpy.data.objects[2]

# muda a lente da camera
camera.data.lens = 30

# remove da cena o objeto 'default'
cena.objects.unlink(cubo)

# alera a intensidade da luz 'default'
lamp.data.energy = 1.2

# muda o tipo para 'sun'
lamp.data.type = 'SUN'

# e a cor
lamp.data.color = (1., .9, .8)

# cria outra fonte de luz
lamp1 = bpy.data.lamps.new('Lamp', type='POINT')
lamp1.energy = 0.5
lamp1.color = (.9, 1., 1.)
_lamp1 = bpy.data.objects.new('Lamp', object_data=lamp1)

# muda o lugar da fonte (default = 0.0, 0.0, 0.0)
_lamp1.location = (6., -6., 6.)

# prende a fonte de luz na cena
cena.objects.link(_lamp1)

# cria um material
material = bpy.data.materials.new('newMat1')
material.diffuse_color = (.38, .33, .28)

# cria uma textura 'quebrada'
textura = bpy.data.textures.new('bump', type='CLOUDS')
textura.noise_scale = 0.25
textura.noise_type = 'SOFT_NOISE'
textura.noise_basis = 'VORONOI_CRACKLE'

# coloca no material
mtex = material.texture_slots.add()
mtex.texture = textura
mtex.texture_coords = 'UV'
mtex.use_map_color_diffuse = False
mtex.use_map_normal = True
mtex.emission_color_factor = 0.5
mtex.use_map_density = True
mtex.mapping = 'SPHERE'

# cria uma esfera
mesh = bpy.ops.mesh.primitive_uv_sphere_add()
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.uv.smart_project()
bpy.ops.object.mode_set(mode='OBJECT')

# coloca o material na esfera
bpy.context.object.data.materials.append(material)

# modo 'blend' no fundo
cena.world.use_sky_blend = True

# altualiza a cena
cena.update()
