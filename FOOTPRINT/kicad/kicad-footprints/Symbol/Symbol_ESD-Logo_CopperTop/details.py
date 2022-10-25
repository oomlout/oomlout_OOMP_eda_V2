
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Symbol"
    oIndex = "Symbol_ESD-Logo_CopperTop"
    hexID = "FZKSZSYESDLCTOP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Symbol_ESD-Logo_CopperTop', 'description': 'ESD-Logo, similar JEDEC-14, without text, ohne Text, Copper Top,', 'tags': 'ESD-Logo, similar JEDEC-14, without text, ohne Text, Copper Top,', 'attributeType': None, 'pins': {}})
    newPart['name'].append('Symbol : Symbol_ESD-Logo_CopperTop')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

