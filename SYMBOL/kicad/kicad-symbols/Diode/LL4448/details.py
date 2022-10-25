
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "LL4448"
    hexID = "SZKDIODELL4448"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LL4148', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'LL4448', 'kicadSymbolFootprint': 'Diode_SMD:D_MiniMELF', 'kicadSymbolDatasheet': 'http://www.vishay.com/docs/85557/ll4148.pdf', 'kicadSymbolki_keywords': 'diode', 'kicadSymbolki_description': '100V 0.15A standard switching diode, MiniMELF', 'kicadSymbolki_fp_filters': 'D*MiniMELF*'}])
    newPart['name'].append('Diode : LL4448')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

