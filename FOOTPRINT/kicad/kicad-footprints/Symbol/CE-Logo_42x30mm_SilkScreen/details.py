
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Symbol"
    oIndex = "CE-Logo_42x30mm_SilkScreen"
    hexID = "FZKSZCEL42X3SILKSCREEN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'CE-Logo_42x30mm_SilkScreen', 'description': 'CE marking', 'tags': 'Logo CE certification', 'attributeType': None, 'pins': {}})
    newPart['name'].append('Symbol : CE-Logo_42x30mm_SilkScreen')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

