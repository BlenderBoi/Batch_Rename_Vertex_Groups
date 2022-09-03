bl_info = {
    "name": "Batch Rename Vertex Groups",
    "author": "BlenderBoi, iJacques",
    "version": (1, 1),
    "blender": (2, 80, 0),
    "location": "View3D > Object > Batch Rename Vertex Groups",
    "description": "Allows you to batch batch rename vertex groups, perfect for when you mess up vertex group or bone naming conventions! Lock vertex groups to exclude them from being renamed",
    "warning": "",
    "doc_url": "https://github.com/BlenderBoi/Batch_Rename_Vertex_Groups",
    "category": "Vertex Group",
}

import bpy


ENUM_Mode = [("PREFIX","Prefix","Prefix"),("SUFFIX","Suffix","Suffix"),("REMOVE","Remove","Remove"), ("REPLACE","Replace","Replace")]


class Batch_Rename_Vertex_Groups(bpy.types.Operator):
    """Batch Rename Vertex Groups"""
    bl_idname = "object.batch_rename_vertex_groups"
    bl_label = "Batch Rename Vertex Groups"
    bl_options = {'UNDO', 'REGISTER'}

    Mode: bpy.props.EnumProperty(items=ENUM_Mode)

    Name01: bpy.props.StringProperty()
    Name02: bpy.props.StringProperty()

    def invoke(self, context, event):

        return context.window_manager.invoke_props_dialog(self)


    def draw(self, context):

        layout = self.layout
        
        layout.prop(self, "Mode",text="Mode")
        
        if self.Mode == "PREFIX":
            layout.prop(self, "Name01", text="Prefix")
        
        if self.Mode == "SUFFIX":
            layout.prop(self, "Name01", text="Suffix")
        
        if self.Mode == "REMOVE":
            layout.prop(self, "Name01", text="Remove")
            
        if self.Mode == "REPLACE":
            layout.prop(self, "Name01", text="Find")
            layout.prop(self, "Name02", text="Replace")    
        
    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        object = context.object
        
        for vertex_group in object.vertex_groups:
            if self.Mode == "PREFIX":
                if vertex_group.lock_weight == False:
                    vertex_group.name = self.Name01 + vertex_group.name
                else: 
                    continue
            if self.Mode == "SUFFIX":
                if vertex_group.lock_weight == False:
                    vertex_group.name = vertex_group.name + self.Name01
                else: 
                    continue
            if self.Mode == "REMOVE":
                if vertex_group.lock_weight == False:
                    vertex_group.name = vertex_group.name.replace(self.Name01, "")
                else: 
                    continue
            if self.Mode == "REPLACE":
                if vertex_group.lock_weight == False:
                    vertex_group.name = vertex_group.name.replace(self.Name01, self.Name02)
                else: 
                    continue
        
        return {'FINISHED'}

def menu_func(self, context):
    self.layout.operator(Batch_Rename_Vertex_Groups.bl_idname, text=Batch_Rename_Vertex_Groups.bl_label)


def register():
    bpy.utils.register_class(Batch_Rename_Vertex_Groups)
    bpy.types.VIEW3D_MT_object.append(menu_func)


def unregister():
    bpy.utils.unregister_class(Batch_Rename_Vertex_Groups)
    bpy.types.VIEW3D_MT_object.remove(menu_func)


if __name__ == "__main__":
    register()
