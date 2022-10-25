
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Symbol"
    oIndex = "UKCA-Logo_40x40mm_SilkScreen"
    hexID = "FZKSZUKCAL4X4SILKSCREEN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'UKCA-Logo_40x40mm_SilkScreen', 'description': 'UKCA marking', 'tags': 'Logo UKCA marking', 'attributeType': None, 'pins': {}})
    newPart['name'].append('Symbol : UKCA-Logo_40x40mm_SilkScreen')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

