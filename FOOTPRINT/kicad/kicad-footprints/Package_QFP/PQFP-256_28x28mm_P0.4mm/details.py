
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_QFP"
    oIndex = "PQFP-256_28x28mm_P0.4mm"
    hexID = "FZKQFPPQFP25628X28P4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'PQFP-256_28x28mm_P0.4mm', 'description': 'PQFP256 28x28 / QFP256J CASE 122BX (see ON Semiconductor 122BX.PDF)', 'tags': 'QFP 0.4', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_QFP.3dshapes/PQFP-256_28x28mm_P0.4mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_QFP : PQFP-256_28x28mm_P0.4mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

