
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Symbol"
    oIndex = "WEEE-Logo_28.1x40mm_SilkScreen"
    hexID = "FZKSZWEEEL281X4SILKSCREEN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'WEEE-Logo_28.1x40mm_SilkScreen', 'description': 'Waste Electrical and Electronic Equipment Directive', 'tags': 'Logo WEEE', 'attributeType': None, 'pins': {}})
    newPart['name'].append('Symbol : WEEE-Logo_28.1x40mm_SilkScreen')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

