
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "LED_THT"
    oIndex = "LED_D3.0mm_Horizontal_O1.27mm_Z2.0mm_IRGrey"
    hexID = "FZKLLD3HORIZONTALO127Z2IRGREY"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LED_D3.0mm_Horizontal_O1.27mm_Z2.0mm_IRGrey', 'description': 'LED, diameter 3.0mm z-position of LED center 2.0mm, 2 pins', 'tags': 'LED diameter 3.0mm z-position of LED center 2.0mm 2 pins', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/LED_THT.3dshapes/LED_D3.0mm_Horizontal_O1.27mm_Z2.0mm_IRGrey.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('LED_THT : LED_D3.0mm_Horizontal_O1.27mm_Z2.0mm_IRGrey')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

