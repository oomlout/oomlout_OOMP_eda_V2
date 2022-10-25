
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "74xx"
    oIndex = "74CBTLV16212"
    hexID = "SZK74XX74CBTLV16212"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': '74CBTLV16212', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.ti.com/lit/ds/symlink/sn74cbtlv16212.pdf', 'kicadSymbolki_keywords': 'bus', 'kicadSymbolki_description': 'Low-voltage 24-bit FET Bus-exchange switch', 'kicadSymbolki_fp_filters': 'SSOP* TSSOP*'}])
    newPart['name'].append('74xx : 74CBTLV16212')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

