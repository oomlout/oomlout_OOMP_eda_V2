
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "Vishay_PowerPAK_1212-8_Dual"
    hexID = "FZKSOVISHAYPOWERPAK12128DUAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Vishay_PowerPAK_1212-8_Dual', 'description': 'PowerPAK 1212-8 Dual (https://www.vishay.com/docs/71656/ppak12128.pdf, https://www.vishay.com/docs/72598/72598.pdf)', 'tags': 'Vishay_PowerPAK_1212-8_Dual', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/Vishay_PowerPAK_1212-8_Dual.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_SO : Vishay_PowerPAK_1212-8_Dual')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

