
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "LED"
    oIndex = "HLCP-J100"
    hexID = "SZKLHLCPJ1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'BAR', 'kicadSymbolValue': 'HLCP-J100', 'kicadSymbolFootprint': 'Display:HLCP-J100', 'kicadSymbolDatasheet': 'https://docs.broadcom.com/docs/AV02-1798EN', 'kicadSymbolki_keywords': 'display LED array', 'kicadSymbolki_description': '10-element LED arrays, AIGaAs Red', 'kicadSymbolki_fp_filters': 'HLCP*J100*'}])
    newPart['name'].append('LED : HLCP-J100')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

