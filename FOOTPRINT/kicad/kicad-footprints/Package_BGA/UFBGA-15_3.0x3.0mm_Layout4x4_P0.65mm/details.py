
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_BGA"
    oIndex = "UFBGA-15_3.0x3.0mm_Layout4x4_P0.65mm"
    hexID = "FZKBGAUFBGA153X3LAYOUT4X4P65"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'UFBGA-15_3.0x3.0mm_Layout4x4_P0.65mm', 'description': 'UFBGA-15, 4x4, 3x3mm package, pitch 0.65mm', 'tags': 'UFBGA-15', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/UFBGA-15_3.0x3.0mm_Layout4x4_P0.65mm.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_BGA : UFBGA-15_3.0x3.0mm_Layout4x4_P0.65mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

