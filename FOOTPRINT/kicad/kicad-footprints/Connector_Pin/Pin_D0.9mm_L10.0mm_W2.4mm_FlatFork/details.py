
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Pin"
    oIndex = "Pin_D0.9mm_L10.0mm_W2.4mm_FlatFork"
    hexID = "FZKCNPINPIND9L1W24FLATFORK"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Pin_D0.9mm_L10.0mm_W2.4mm_FlatFork', 'description': 'solder Pin_ with flat fork, hole diameter 0.9mm, length 10.0mm, width 2.4mm', 'tags': 'solder Pin_ with flat fork', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Pin.3dshapes/Pin_D0.9mm_L10.0mm_W2.4mm_FlatFork.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Pin : Pin_D0.9mm_L10.0mm_W2.4mm_FlatFork')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

