
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "74xx"
    oIndex = "74LS46"
    hexID = "SZK74XX74LS46"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '74LS47', 'kicadSymbolReference': 'U', 'kicadSymbolValue': '74LS46', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/gpn/sn74LS46', 'kicadSymbolki_keywords': 'TTL DECOD DECOD7 OpenCol', 'kicadSymbolki_description': 'BCD to 7-segment Driver, Open Collector, 15V outputs', 'kicadSymbolki_fp_filters': 'DIP?16*'}])
    newPart['name'].append('74xx : 74LS46')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

