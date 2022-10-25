
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "SM4002"
    hexID = "SZKDIODESM42"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SM4001', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'SM4002', 'kicadSymbolFootprint': 'Diode_SMD:D_MELF', 'kicadSymbolDatasheet': 'http://cdn-reichelt.de/documents/datenblatt/A400/SMD1N400%23DIO.pdf', 'kicadSymbolki_keywords': 'diode', 'kicadSymbolki_description': '100V 1A General Purpose Rectifier Diode, MELF', 'kicadSymbolki_fp_filters': 'D*MELF*'}])
    newPart['name'].append('Diode : SM4002')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

