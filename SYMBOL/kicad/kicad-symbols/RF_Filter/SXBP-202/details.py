
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Filter"
    oIndex = "SXBP-202"
    hexID = "SZKRFFILSXBP22"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SXBP-140', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SXBP-202', 'kicadSymbolFootprint': 'RF_Mini-Circuits:Mini-Circuits_HF1139_LandPatternPL-230', 'kicadSymbolDatasheet': 'https://www.minicircuits.com/pdfs/SXBP-202+.pdf', 'kicadSymbolki_keywords': 'bandpass filter', 'kicadSymbolki_description': 'Bandpass Filter, 198 to 206 MHz, 50 Ohm, Mini-Circuits HF1139', 'kicadSymbolki_fp_filters': 'Mini?Circuits*HF1139*'}])
    newPart['name'].append('RF_Filter : SXBP-202')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

