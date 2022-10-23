
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Oscillator"
    oIndex = "JTOS-25"
    hexID = "SZKOCSJTOS25"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'JTOS-50', 'kicadSymbolReference': 'X', 'kicadSymbolValue': 'JTOS-25', 'kicadSymbolFootprint': 'RF_Mini-Circuits:Mini-Circuits_BK377_LandPatternPL-005', 'kicadSymbolDatasheet': 'https://www.minicircuits.com/pdfs/JTOS-25+.pdf', 'kicadSymbolki_keywords': 'VCXO', 'kicadSymbolki_description': 'Voltage Controlled Oscillator, 12.5 to 25 MHz, Mini-Circuits BK377', 'kicadSymbolki_fp_filters': 'Mini?Circuits*BK377*'}])
    newPart['name'].append('JTOS-25')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

