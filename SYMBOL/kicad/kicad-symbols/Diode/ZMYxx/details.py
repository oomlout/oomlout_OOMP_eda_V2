
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "ZMYxx"
    hexID = "SZKDIODEZMYXX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ZPYxx', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'ZMYxx', 'kicadSymbolFootprint': 'Diode_SMD:D_MELF', 'kicadSymbolDatasheet': 'https://www.vishay.com/docs/85788/zmy3v9.pdf', 'kicadSymbolki_keywords': 'zener diode', 'kicadSymbolki_description': '1300mW Zener Diode, MELF', 'kicadSymbolki_fp_filters': 'D*MELF*'}])
    newPart['name'].append('Diode : ZMYxx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

