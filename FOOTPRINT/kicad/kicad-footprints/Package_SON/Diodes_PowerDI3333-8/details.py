
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SON"
    oIndex = "Diodes_PowerDI3333-8"
    hexID = "FZKSONDIODESPOWERDI33338"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Diodes_PowerDI3333-8', 'description': 'Diodes Incorporated PowerDI3333-8, Plastic Dual Flat No Lead Package, 3.3x3.3x0.8mm Body, https://www.diodes.com/assets/Package-Files/PowerDI3333-8.pdf', 'tags': 'PowerDI 0.65', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SON.3dshapes/Diodes_PowerDI3333-8.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_SON : Diodes_PowerDI3333-8')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

