
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "BAS516"
    hexID = "SZKDIODEBAS516"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '1N4001', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'BAS516', 'kicadSymbolFootprint': 'Diode_SMD:D_SOD-523', 'kicadSymbolDatasheet': 'https://assets.nexperia.com/documents/data-sheet/BAS16_SER.pdf', 'kicadSymbolki_keywords': 'diode', 'kicadSymbolki_description': '100V, 0.25A, High-speed Switching Diode, SOD-523', 'kicadSymbolki_fp_filters': 'D*SOD?523*'}])
    newPart['name'].append('BAS516')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

