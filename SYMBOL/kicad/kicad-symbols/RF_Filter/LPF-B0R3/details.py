
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Filter"
    oIndex = "LPF-B0R3"
    hexID = "SZKRFFILLPFBR3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LPF-B0R3', 'kicadSymbolFootprint': 'RF_Mini-Circuits:Mini-Circuits_HZ1198_LandPatternPL-247', 'kicadSymbolDatasheet': 'https://www.minicircuits.com/pdfs/LPF-B0R3+.pdf', 'kicadSymbolki_keywords': 'low pass filter', 'kicadSymbolki_description': 'Low Pass Filter, DC to 0.3 MHz, 50 Ohm, Mini-Circuits HZ1198', 'kicadSymbolki_fp_filters': 'Mini?Circuits*HZ1198*'}])
    newPart['name'].append('RF_Filter : LPF-B0R3')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

