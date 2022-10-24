
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_TO_SOT_THT"
    oIndex = "SOT-227"
    hexID = "FZKSOTSOT227"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SOT-227', 'description': 'SOT-227 / SOT-227B / ISOTOP, M4 mounting screws (https://www.vishay.com/docs/95423/sot227g2.pdf, https://www.vishay.com/docs/95793/vs-fc420sa10.pdf)', 'tags': 'sot 227 isotop', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_TO_SOT_THT.3dshapes/SOT-227.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_TO_SOT_THT : SOT-227')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

