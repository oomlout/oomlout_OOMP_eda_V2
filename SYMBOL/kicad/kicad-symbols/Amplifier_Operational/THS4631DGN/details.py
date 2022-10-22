
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "THS4631DGN"
    hexID = "SZKAMPLIFIEROPERATIONALTHS4631DGN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'THS4631DDA', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'THS4631DGN', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'www.ti.com/lit/ds/symlink/ths4631.pdf', 'kicadSymbolki_keywords': 'single opamp', 'kicadSymbolki_description': 'Single High-voltage, High Slew Rate, Wideband, FET-input Operational Amplifier, MSOP-8', 'kicadSymbolki_fp_filters': 'SOIC*1EP*3.9x4.9mm*P1.27mm* MSOP*1EP*3x3mm*P0.65mm*'}])
    newPart['name'].append('THS4631DGN')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

