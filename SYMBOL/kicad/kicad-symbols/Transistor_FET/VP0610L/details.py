
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "VP0610L"
    hexID = "SZKTRANSISTORFETVP61L"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TP0610L', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'VP0610L', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-92L_Inline', 'kicadSymbolDatasheet': 'http://www.vishay.com/docs/70209/70209.pdf', 'kicadSymbolki_keywords': 'P-Channel MOSFET', 'kicadSymbolki_description': '-0.18A Id, -60V Vds, P-Channel MOSFET, TO-92', 'kicadSymbolki_fp_filters': 'TO?92L*'}])
    newPart['name'].append('Transistor_FET : VP0610L')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

