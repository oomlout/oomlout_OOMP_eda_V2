
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "LED_SMD"
    oIndex = "LED_Kingbright_KPBD-3224"
    hexID = "FZKLSMLKINGBRIGHTKPBD3224"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LED_Kingbright_KPBD-3224', 'description': 'Kingbright, dual LED, red-green, dome lens, 3.2 x 2.4 mm Surface Mount LED Lamp (https://www.kingbright.com/attachments/file/psearch/000/00/00/KPBD-3224SURKCGKC(Ver.20A).pdf)', 'tags': 'Kingbright dual LED KPBD-3224', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/LED_SMD.3dshapes/LED_Kingbright_KPBD-3224.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('LED_SMD : LED_Kingbright_KPBD-3224')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

