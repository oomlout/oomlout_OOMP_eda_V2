
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Mixer"
    oIndex = "ADE-6"
    hexID = "SZKRFMIXERADE6"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADE-6', 'kicadSymbolFootprint': 'RF_Mini-Circuits:Mini-Circuits_CD542_LandPatternPL-052', 'kicadSymbolDatasheet': 'https://www.minicircuits.com/pdfs/ADE-6.pdf', 'kicadSymbolki_keywords': 'mixer rf', 'kicadSymbolki_description': 'Mixer, +7 dBm LO, 0.05 to 250 MHz, CD542', 'kicadSymbolki_fp_filters': 'Mini?Circuits*CD542*'}])
    newPart['name'].append('ADE-6')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

