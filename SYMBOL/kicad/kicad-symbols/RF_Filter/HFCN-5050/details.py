
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Filter"
    oIndex = "HFCN-5050"
    hexID = "SZKRFFILHFCN55"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'HFCN-672', 'kicadSymbolReference': 'FL', 'kicadSymbolValue': 'HFCN-5050', 'kicadSymbolFootprint': 'Filter:Filter_Mini-Circuits_FV1206-1', 'kicadSymbolDatasheet': 'https://www.minicircuits.com/pdfs/HFCN-5050+.pdf', 'kicadSymbolki_keywords': 'Mini-Circuits high pass filter', 'kicadSymbolki_description': '5050MHz 50 Ohm Passive High Pass Filter, FV1206-1', 'kicadSymbolki_fp_filters': 'Filter*Mini?Circuits*FV1206?1*'}])
    newPart['name'].append('RF_Filter : HFCN-5050')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

