
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_TO_SOT_THT"
    oIndex = "TO-220-9_P1.94x3.7mm_StaggerEven_Lead3.8mm_Vertical"
    hexID = "FZKSOTTO229P194X37STAGGEREVENLEAD38VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TO-220-9_P1.94x3.7mm_StaggerEven_Lead3.8mm_Vertical', 'description': 'TO-220-9, Vertical, RM 0.97mm, Multiwatt-9, staggered type-2', 'tags': 'TO-220-9 Vertical RM 0.97mm Multiwatt-9 staggered type-2', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_TO_SOT_THT.3dshapes/TO-220-9_P1.94x3.7mm_StaggerEven_Lead3.8mm_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Package_TO_SOT_THT : TO-220-9_P1.94x3.7mm_StaggerEven_Lead3.8mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

