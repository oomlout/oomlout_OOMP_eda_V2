
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "LED_THT"
    oIndex = "LED_D3.0mm-3"
    hexID = "FZKLLD33"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LED_D3.0mm-3', 'description': 'LED, diameter 3.0mm, 2 pins, diameter 3.0mm, 3 pins, http://www.kingbright.com/attachments/file/psearch/000/00/00/L-3VSURKCGKC(Ver.8A).pdf', 'tags': 'LED diameter 3.0mm 2 pins diameter 3.0mm 3 pins', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/LED_THT.3dshapes/LED_D3.0mm-3.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('LED_THT : LED_D3.0mm-3')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

