
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_TO_SOT_THT"
    oIndex = "TO-220F-4_P5.08x3.7mm_StaggerEven_Lead3.5mm_Vertical"
    hexID = "FZKSOTTO22F4P58X37STAGGEREVENLEAD35VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TO-220F-4_P5.08x3.7mm_StaggerEven_Lead3.5mm_Vertical', 'description': 'TO-220F-4, Vertical, RM 2.54mm, staggered type-2, see https://www.njr.com/semicon/PDF/package/TO-220F-4_E.pdf', 'tags': 'TO-220F-4 Vertical RM 2.54mm staggered type-2', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_TO_SOT_THT.3dshapes/TO-220F-4_P5.08x3.7mm_StaggerEven_Lead3.5mm_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Package_TO_SOT_THT : TO-220F-4_P5.08x3.7mm_StaggerEven_Lead3.5mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

