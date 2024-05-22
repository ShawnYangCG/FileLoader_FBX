# this script needs Autodesk FBX SDK
import fbx

class FBX:
    def __init__(self, file_path):
        self.file_path = file_path
        self.manager = fbx.FbxManager.Create()
        self.scene = fbx.FbxScene.Create(self.manager, "Scene")

        self.importer = fbx.FbxImporter.Create(self.manager, "Importer")
        if not self.importer.Initialize(self.file_path, -1, self.manager.GetIOSettings()):
            raise Exception(f"Failed to initialize the importer for {self.file_path}")

        if not self.importer.Import(self.scene):
            raise Exception(f"Failed to import the FBX file: {self.file_path}")

        self.importer.Destroy()

    def print_scene_info(self):
        root_node = self.scene.GetRootNode()
        if root_node:
            self._print_node_info(root_node)

    def _print_node_info(self, node, depth=0):
        print("  " * depth + node.GetName())
        for i in range(node.GetChildCount()):
            self._print_node_info(node.GetChild(i), depth + 1)

# 使用示例
fbx_reader = FBX("data//bow.fbx")
fbx_reader.print_scene_info()
