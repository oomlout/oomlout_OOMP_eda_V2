
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "74xx"
    oIndex = "74LS156"
    hexID = "SZK74XX74LS156"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '74LS155', 'kicadSymbolReference': 'U', 'kicadSymbolValue': '74LS156', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/gpn/sn74LS156', 'kicadSymbolki_keywords': 'TTL DECOD8 DECOD4 DEMUX4 DEMUX8 OpenCol', 'kicadSymbolki_description': 'Dual 2 to 4 lines Decoder/Demultiplexer, Open Collector', 'kicadSymbolki_fp_filters': 'DIP?16*'}])
    newPart['name'].append('74xx : 74LS156')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

