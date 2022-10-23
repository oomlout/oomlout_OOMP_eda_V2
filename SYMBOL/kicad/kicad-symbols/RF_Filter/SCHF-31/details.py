
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Filter"
    oIndex = "SCHF-31"
    hexID = "SZKRFFILSCHF31"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SCHF-31', 'kicadSymbolFootprint': 'RF_Mini-Circuits:Mini-Circuits_YY161_LandPatternPL-049', 'kicadSymbolDatasheet': 'https://www.minicircuits.com/pdfs/SCHF-31+.pdf', 'kicadSymbolki_keywords': 'highpass filter rf', 'kicadSymbolki_description': 'High Pass Filter, 31 to 1500 MHz, 50 Ohm, Mini-Circuits YY161', 'kicadSymbolki_fp_filters': 'Mini?Circuits*YY161*'}])
    newPart['name'].append('SCHF-31')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

