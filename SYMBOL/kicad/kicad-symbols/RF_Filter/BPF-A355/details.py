
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Filter"
    oIndex = "BPF-A355"
    hexID = "SZKRFFILBPFA355"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'BPF-A355', 'kicadSymbolFootprint': 'RF_Mini-Circuits:Mini-Circuits_HQ1157', 'kicadSymbolDatasheet': 'https://www.minicircuits.com/pdfs/BPF-A355+.pdf', 'kicadSymbolki_keywords': 'Bandpass Filter', 'kicadSymbolki_description': 'Bandpass Filter, 310 to 400 MHz, 50 Ohm, Mini-Circuits HQ1157', 'kicadSymbolki_fp_filters': 'Mini?Circuits*HQ1157*'}])
    newPart['name'].append('BPF-A355')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

