
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Difference"
    oIndex = "AD628"
    hexID = "SZKAMPLIFIERDIFFERENCEAD628"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AD628', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/AD628.pdf', 'kicadSymbolki_keywords': 'difference amplifier', 'kicadSymbolki_description': 'High Common-Mode Voltage, Programmable Gain Difference Amplifier, +/-120V, Gain = 0.1 to 100, SOIC-8/MSOP-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm* MSOP*3x3mm*P0.65mm*'}])
    newPart['name'].append('Amplifier_Difference : AD628')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

