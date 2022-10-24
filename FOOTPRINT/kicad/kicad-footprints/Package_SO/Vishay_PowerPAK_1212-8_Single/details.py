
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "Vishay_PowerPAK_1212-8_Single"
    hexID = "FZKSOVISHAYPOWERPAK12128SINGLE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Vishay_PowerPAK_1212-8_Single', 'description': 'PowerPAK 1212-8 Single (https://www.vishay.com/docs/71656/ppak12128.pdf, https://www.vishay.com/docs/72597/72597.pdf)', 'tags': 'Vishay PowerPAK 1212-8 Single', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/Vishay_PowerPAK_1212-8_Single.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_SO : Vishay_PowerPAK_1212-8_Single')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

