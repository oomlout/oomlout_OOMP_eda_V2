
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "SSOP-8_3.95x5.21x3.27mm_P1.27mm"
    hexID = "FZKSOSS8395X521X327P127"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SSOP-8_3.95x5.21x3.27mm_P1.27mm', 'description': 'SSOP-8 3.95x5.21x3.27mm Pitch 1.27mm', 'tags': 'SSOP-8 3.95x5.21x3.27mm 1.27mm', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/SSOP-8_3.95x5.21x3.27mm_P1.27mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_SO : SSOP-8_3.95x5.21x3.27mm_P1.27mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

