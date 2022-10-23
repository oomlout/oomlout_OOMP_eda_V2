
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Pin"
    oIndex = "Pin_D1.1mm_L10.2mm_W3.5mm_Flat"
    hexID = "FZKCNPINPIND11L12W35FLAT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Pin_D1.1mm_L10.2mm_W3.5mm_Flat', 'description': 'solder Pin_ with flat with hole, hole diameter 1.1mm, length 10.2mm, width 3.5mm', 'tags': 'solder Pin_ with flat fork', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Pin.3dshapes/Pin_D1.1mm_L10.2mm_W3.5mm_Flat.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Pin : Pin_D1.1mm_L10.2mm_W3.5mm_Flat')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

