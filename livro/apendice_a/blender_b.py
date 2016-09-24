#!/usr/python3.5
# exemplo com interface
import bpy

# painel para aparecer nas ferramentas
class Panel (bpy.types.Panel):
    bl_label = 'Cria objetos'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'

    def draw (self, context):
        # interface
        linha = self.layout.row()
        caixa = linha.box()

        # tres botoes
        caixa.operator('cria.objeto', text='Cubo').objeto = 'cubo'
        caixa.operator('cria.objeto', text='Esfera').objeto = 'esfera'
        caixa.operator('cria.objeto', text='Refeltor').objeto = 'area'

class CriaObjeto (bpy.types.Operator):
    # o id deve ter um ponto
    bl_idname = 'cria.objeto'
    bl_label = 'Cria objeto'

    # uma proprieddade no blender
    objeto = bpy.props.StringProperty()

    # funcoa que sera executada pela interface
    def execute (self, context):
        if self.objeto == 'cubo':
            bpy.ops.mesh.primitive_cube_add()
        elif self.objeto == 'esfera':
            bpy.ops.mesh.primitive_uv_sphere_add()
        elif self.objeto == 'area':
            cena = bpy.data.scenes[0]
            lamp1 = bpy.data.lamps.new('Lamp', type='AREA')
            _lamp1 = bpy.data.objects.new('Lamp', object_data=lamp1)
            cena.objects.link(_lamp1)
        # termina o processamento
        return {'FINISHED'}

# registra o modulo na interface do blender
bpy.utils.register_module(__name__)

