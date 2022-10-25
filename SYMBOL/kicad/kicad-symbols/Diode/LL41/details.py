
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "LL41"
    hexID = "SZKDIODELL41"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'LL41', 'kicadSymbolFootprint': 'Diode_SMD:D_MiniMELF', 'kicadSymbolDatasheet': 'http://www.vishay.com/docs/85659/bat41.pdf', 'kicadSymbolki_keywords': 'diode Schottky', 'kicadSymbolki_description': '100V 0.1A Small Signal Schottky diode, MiniMELF', 'kicadSymbolki_fp_filters': 'D*MiniMELF*'}])
    newPart['name'].append('Diode : LL41')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

