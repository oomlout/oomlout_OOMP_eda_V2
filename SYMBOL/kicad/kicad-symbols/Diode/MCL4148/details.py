
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "MCL4148"
    hexID = "SZKDIODEMCL4148"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'MCL4148', 'kicadSymbolFootprint': 'Diode_SMD:D_MicroMELF', 'kicadSymbolDatasheet': 'http://www.vishay.com/docs/85566/mlc4148.pdf', 'kicadSymbolki_keywords': 'diode', 'kicadSymbolki_description': '75V 0.2A Switching Diode, MicroMELF', 'kicadSymbolki_fp_filters': 'D*MicroMELF*'}])
    newPart['name'].append('Diode : MCL4148')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

