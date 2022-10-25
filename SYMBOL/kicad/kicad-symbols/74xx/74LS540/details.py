
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "74xx"
    oIndex = "74LS540"
    hexID = "SZK74XX74LS54"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': '74LS540', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/gpn/sn74LS540', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'BUFFER BUS TTL 3State', 'kicadSymbolki_description': '8-bit Buffer/Line driver Inverter, 3-state outputs', 'kicadSymbolki_fp_filters': 'DIP?20*'}])
    newPart['name'].append('74xx : 74LS540')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

