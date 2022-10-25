
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "BZV55C47"
    hexID = "SZKDIODEBZV55C47"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ZPYxx', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'BZV55C47', 'kicadSymbolFootprint': 'Diode_SMD:D_MiniMELF', 'kicadSymbolDatasheet': 'https://assets.nexperia.com/documents/data-sheet/BZV55_SER.pdf', 'kicadSymbolki_keywords': 'zener diode', 'kicadSymbolki_description': '47V, 500mW, 5%, Zener diode, MiniMELF', 'kicadSymbolki_fp_filters': 'D*MiniMELF*'}])
    newPart['name'].append('Diode : BZV55C47')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

