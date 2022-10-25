
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Symbol"
    oIndex = "KiCad-Logo_8mm_Copper"
    hexID = "FZKSZKICADL8C"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'KiCad-Logo_8mm_Copper', 'description': 'KiCad Logo', 'tags': 'Logo KiCad', 'attributeType': None, 'pins': {}})
    newPart['name'].append('Symbol : KiCad-Logo_8mm_Copper')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

