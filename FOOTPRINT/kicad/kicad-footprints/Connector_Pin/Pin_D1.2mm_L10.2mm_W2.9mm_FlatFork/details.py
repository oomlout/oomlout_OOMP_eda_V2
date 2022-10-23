
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Pin"
    oIndex = "Pin_D1.2mm_L10.2mm_W2.9mm_FlatFork"
    hexID = "FZKCNPINPIND12L12W29FLATFORK"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Pin_D1.2mm_L10.2mm_W2.9mm_FlatFork', 'description': 'solder Pin_ with flat with fork, hole diameter 1.2mm, length 11.3mm, width 3.0mm', 'tags': 'solder Pin_ with flat fork', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Pin.3dshapes/Pin_D1.2mm_L10.2mm_W2.9mm_FlatFork.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Pin : Pin_D1.2mm_L10.2mm_W2.9mm_FlatFork')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

