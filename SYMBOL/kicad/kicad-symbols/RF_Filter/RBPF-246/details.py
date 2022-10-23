
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Filter"
    oIndex = "RBPF-246"
    hexID = "SZKRFFILRBPF246"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'RBPF-246', 'kicadSymbolFootprint': 'RF_Mini-Circuits:Mini-Circuits_CK605_LandPatternPL-012', 'kicadSymbolDatasheet': 'https://www.minicircuits.com/pdfs/RBPF-246+.pdf', 'kicadSymbolki_keywords': 'Bandpass Filter', 'kicadSymbolki_description': 'Bandpass Filter, 236 to 265 MHz, 50 Ohm, Mini-Circuits CK605', 'kicadSymbolki_fp_filters': 'Mini?Circuits*CK605*'}])
    newPart['name'].append('RBPF-246')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

