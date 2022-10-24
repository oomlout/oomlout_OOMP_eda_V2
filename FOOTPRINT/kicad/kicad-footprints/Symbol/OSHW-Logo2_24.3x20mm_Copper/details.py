
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Symbol"
    oIndex = "OSHW-Logo2_24.3x20mm_Copper"
    hexID = "FZKSZOSHWL2243X2C"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'OSHW-Logo2_24.3x20mm_Copper', 'description': 'Open Source Hardware Symbol', 'tags': 'Logo Symbol OSHW', 'attributeType': None, 'pins': {}})
    newPart['name'].append('Symbol : OSHW-Logo2_24.3x20mm_Copper')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

