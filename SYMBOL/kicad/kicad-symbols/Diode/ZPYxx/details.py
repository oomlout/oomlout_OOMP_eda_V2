
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "ZPYxx"
    hexID = "SZKDIODEZPYXX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'ZPYxx', 'kicadSymbolFootprint': 'Diode_THT:D_DO-41_SOD81_P10.16mm_Horizontal', 'kicadSymbolDatasheet': 'http://www.vishay.com/docs/85790/zpy3v9.pdf', 'kicadSymbolki_keywords': 'zener diode', 'kicadSymbolki_description': '1300mW Zener Diode, DO-41', 'kicadSymbolki_fp_filters': 'D*DO?41*'}])
    newPart['name'].append('Diode : ZPYxx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

