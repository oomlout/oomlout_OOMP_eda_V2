
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "UDFN-9_1.0x3.8mm_P0.5mm"
    hexID = "FZKDFNUDFN91X38P5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'UDFN-9_1.0x3.8mm_P0.5mm', 'description': '9-pin UDFN package, 1.0x3.8mm, (Ref: https://katalog.we-online.de/pbs/datasheet/824014881.pdf)', 'tags': 'UDFN SMD', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/UDFN-9_1.0x3.8mm_P0.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DFN_QFN : UDFN-9_1.0x3.8mm_P0.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

