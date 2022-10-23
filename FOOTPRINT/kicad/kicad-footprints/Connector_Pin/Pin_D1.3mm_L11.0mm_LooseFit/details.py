
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Pin"
    oIndex = "Pin_D1.3mm_L11.0mm_LooseFit"
    hexID = "FZKCNPINPIND13L11LOOSEFIT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Pin_D1.3mm_L11.0mm_LooseFit', 'description': 'solder Pin_ diameter 1.3mm, hole diameter 1.5mm (loose fit), length 11.0mm', 'tags': 'solder Pin_ loose fit', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Pin.3dshapes/Pin_D1.3mm_L11.0mm_LooseFit.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Pin : Pin_D1.3mm_L11.0mm_LooseFit')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

