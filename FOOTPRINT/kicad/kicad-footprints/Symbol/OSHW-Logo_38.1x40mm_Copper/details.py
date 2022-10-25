
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Symbol"
    oIndex = "OSHW-Logo_38.1x40mm_Copper"
    hexID = "FZKSZOSHWL381X4C"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'OSHW-Logo_38.1x40mm_Copper', 'description': 'Open Source Hardware Logo', 'tags': 'Logo OSHW', 'attributeType': None, 'pins': {}})
    newPart['name'].append('Symbol : OSHW-Logo_38.1x40mm_Copper')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

