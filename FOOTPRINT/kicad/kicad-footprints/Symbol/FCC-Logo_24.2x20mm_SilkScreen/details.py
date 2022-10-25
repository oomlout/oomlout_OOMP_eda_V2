
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Symbol"
    oIndex = "FCC-Logo_24.2x20mm_SilkScreen"
    hexID = "FZKSZFCCL242X2SILKSCREEN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'FCC-Logo_24.2x20mm_SilkScreen', 'description': 'FCC marking', 'tags': 'Logo FCC certification', 'attributeType': None, 'pins': {}})
    newPart['name'].append('Symbol : FCC-Logo_24.2x20mm_SilkScreen')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

