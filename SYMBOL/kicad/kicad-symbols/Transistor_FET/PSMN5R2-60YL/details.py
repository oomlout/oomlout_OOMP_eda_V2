
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "PSMN5R2-60YL"
    hexID = "SZKTRANSISTORFETPSMN5R26YL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'PSMN5R2-60YL', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:LFPAK56', 'kicadSymbolDatasheet': 'https://assets.nexperia.com/documents/data-sheet/PSMN5R2-60YL.pdf', 'kicadSymbolki_keywords': 'N-Channel MOSFET', 'kicadSymbolki_description': '100A, 60V Vds, N-Channel MOSFET, 5.2mOhm Ron, LFPAK56', 'kicadSymbolki_fp_filters': 'LFPAK56*'}])
    newPart['name'].append('Transistor_FET : PSMN5R2-60YL')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

