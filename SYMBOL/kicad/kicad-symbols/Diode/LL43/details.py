
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "LL43"
    hexID = "SZKDIODELL43"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LL41', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'LL43', 'kicadSymbolFootprint': 'Diode_SMD:D_MiniMELF', 'kicadSymbolDatasheet': 'http://www.vishay.com/docs/85672/ll42.pdf', 'kicadSymbolki_keywords': 'diode Schottky', 'kicadSymbolki_description': '30V 0.2A Small Signal Schottky diode, MiniMELF', 'kicadSymbolki_fp_filters': 'D*MiniMELF*'}])
    newPart['name'].append('Diode : LL43')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

