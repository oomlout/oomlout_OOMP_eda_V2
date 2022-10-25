
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_BGA"
    oIndex = "VFBGA-86_6x6mm_Layout10x10_P0.55mm_Ball0.25mm_Pad0.2mm"
    hexID = "FZKBGAVFBGA866X6LAYOUT1X1P55BALL25PAD2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'VFBGA-86_6x6mm_Layout10x10_P0.55mm_Ball0.25mm_Pad0.2mm', 'description': 'VFBGA-86, 6.0x6.0mm, 86 Ball, 10x10 Layout, 0.55mm Pitch, https://www.dialog-semiconductor.com/sites/default/files/da1469x_datasheet_3v1.pdf#page=740', 'tags': 'BGA 86 0.55', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/VFBGA-86_6x6mm_Layout10x10_P0.55mm_Ball0.25mm_Pad0.2mm.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_BGA : VFBGA-86_6x6mm_Layout10x10_P0.55mm_Ball0.25mm_Pad0.2mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

