
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Mixer"
    oIndex = "ADEX-10"
    hexID = "SZKRFMIXERADEX1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ADE-6', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADEX-10', 'kicadSymbolFootprint': 'RF_Mini-Circuits:Mini-Circuits_CD542_LandPatternPL-052', 'kicadSymbolDatasheet': 'https://www.minicircuits.com/pdfs/ADEX-10.pdf', 'kicadSymbolki_keywords': 'mixer rf', 'kicadSymbolki_description': 'Mixer, +7 dBm LO, 10 to 1000 MHz, CD542', 'kicadSymbolki_fp_filters': 'Mini?Circuits*CD542*'}])
    newPart['name'].append('ADEX-10')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

