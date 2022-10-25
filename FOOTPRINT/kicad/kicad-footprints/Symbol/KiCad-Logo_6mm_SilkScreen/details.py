
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Symbol"
    oIndex = "KiCad-Logo_6mm_SilkScreen"
    hexID = "FZKSZKICADL6SILKSCREEN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'KiCad-Logo_6mm_SilkScreen', 'description': 'KiCad Logo', 'tags': 'Logo KiCad', 'attributeType': None, 'pins': {}})
    newPart['name'].append('Symbol : KiCad-Logo_6mm_SilkScreen')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

