
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Filter"
    oIndex = "HFCN-3800D"
    hexID = "SZKRFFILHFCN38D"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'HFCN-672', 'kicadSymbolReference': 'FL', 'kicadSymbolValue': 'HFCN-3800D', 'kicadSymbolFootprint': 'Filter:Filter_Mini-Circuits_FV1206-1', 'kicadSymbolDatasheet': 'https://www.minicircuits.com/pdfs/HFCN-3800D+.pdf', 'kicadSymbolki_keywords': 'Mini-Circuits high pass filter', 'kicadSymbolki_description': '3800MHz 50 Ohm Passive High Pass Filter, DC capable, FV1206-1', 'kicadSymbolki_fp_filters': 'Filter*Mini?Circuits*FV1206?1*'}])
    newPart['name'].append('RF_Filter : HFCN-3800D')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

