
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Filter"
    oIndex = "RBP-280"
    hexID = "SZKRFFILRBP28"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'RBP-280', 'kicadSymbolFootprint': 'RF_Mini-Circuits:Mini-Circuits_GP731_LandPatternPL-176', 'kicadSymbolDatasheet': 'https://www.minicircuits.com/pdfs/RBP-280+.pdf', 'kicadSymbolki_keywords': 'bandpass filter rf', 'kicadSymbolki_description': 'Bandpass Filter, 260 to 310 MHz, 50 Ohm, Mini-Circuits GP731', 'kicadSymbolki_fp_filters': 'Mini?Circuits*GP731*'}])
    newPart['name'].append('RBP-280')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

