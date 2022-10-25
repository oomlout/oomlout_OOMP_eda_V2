
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Symbol"
    oIndex = "Symbol_ESD-Logo-Text_CopperTop"
    hexID = "FZKSZSYESDLTEXTCTOP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Symbol_ESD-Logo-Text_CopperTop', 'tags': None, 'attributeType': None, 'pins': {}})
    newPart['name'].append('Symbol : Symbol_ESD-Logo-Text_CopperTop')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

