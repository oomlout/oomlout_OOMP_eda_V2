
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Pin"
    oIndex = "Pin_D1.1mm_L8.5mm_W2.5mm_FlatFork"
    hexID = "FZKCNPINPIND11L85W25FLATFORK"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Pin_D1.1mm_L8.5mm_W2.5mm_FlatFork', 'description': 'solder Pin_ with flat fork, hole diameter 1.1mm, length 8.5mm, width 2.5mm', 'tags': 'solder Pin_ with flat fork', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Pin.3dshapes/Pin_D1.1mm_L8.5mm_W2.5mm_FlatFork.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Pin : Pin_D1.1mm_L8.5mm_W2.5mm_FlatFork')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

