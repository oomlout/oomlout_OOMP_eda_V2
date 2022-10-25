
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Filter"
    oIndex = "SXBP-140"
    hexID = "SZKRFFILSXBP14"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SXBP-140', 'kicadSymbolFootprint': 'RF_Mini-Circuits:Mini-Circuits_HF1139_LandPatternPL-230', 'kicadSymbolDatasheet': 'https://www.minicircuits.com/pdfs/SXBP-140+.pdf', 'kicadSymbolki_keywords': 'Mini-Circuits Band-Pass Filter', 'kicadSymbolki_description': 'Bandpass Filter, 130 to 150 MHz, 50 Ohm, Mini-Circuits HF1139', 'kicadSymbolki_fp_filters': 'Mini?Circuits*HF1139*'}])
    newPart['name'].append('RF_Filter : SXBP-140')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

