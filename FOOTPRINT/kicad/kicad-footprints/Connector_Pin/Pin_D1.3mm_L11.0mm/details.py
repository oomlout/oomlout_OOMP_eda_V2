
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Pin"
    oIndex = "Pin_D1.3mm_L11.0mm"
    hexID = "FZKCNPINPIND13L11"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Pin_D1.3mm_L11.0mm', 'description': 'solder Pin_ diameter 1.3mm, hole diameter 1.3mm, length 11.0mm', 'tags': 'solder Pin_ pressfit', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Pin.3dshapes/Pin_D1.3mm_L11.0mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Pin : Pin_D1.3mm_L11.0mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

