# FileLoader_FBX
A fileloader to read, edit, and save 3D fbx files.

## Usage 
This loader has two method to process fbx file. 

**1. Using Autodesk FBX SDK**
   - **fbxLoader.py** used for reading fbx file.


**2. Using blender API**
   - All blender scripts are stored in **blender_script** folder. Make sure you have **blender** been installed and the environment PATH been set before you run the script.

```bash
blender --python get_body_model.py
blender --python get_sequence.py
```

   - This script read data from fbx file and convert it into npz file for numpy to read. 
   - The idea of this method was comes from *hbertiche*'s project **NeuralClothSim**.
   - For more detail please look at the source: https://github.com/hbertiche/NeuralClothSim
