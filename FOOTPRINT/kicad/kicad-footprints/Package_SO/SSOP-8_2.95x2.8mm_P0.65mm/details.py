
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "SSOP-8_2.95x2.8mm_P0.65mm"
    hexID = "FZKSOSS8295X28P65"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SSOP-8_2.95x2.8mm_P0.65mm', 'description': 'SSOP-8 2.9 x2.8mm Pitch 0.65mm', 'tags': 'SSOP-8 2.95x2.8mm Pitch 0.65mm', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/SSOP-8_2.95x2.8mm_P0.65mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_SO : SSOP-8_2.95x2.8mm_P0.65mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

