
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_IGBT"
    oIndex = "IRG4PF50W"
    hexID = "SZKTRANSISTORIGBTIRG4PF5W"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IRG4PF50W', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-247-3_Vertical', 'kicadSymbolDatasheet': 'http://www.irf.com/product-info/datasheets/data/irg4pf50w.pdf', 'kicadSymbolki_keywords': 'N-Channel IGBT Power Transistor', 'kicadSymbolki_description': '28A, 900V, N-Channel IGBT', 'kicadSymbolki_fp_filters': 'TO?247*'}])
    newPart['name'].append('IRG4PF50W')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

