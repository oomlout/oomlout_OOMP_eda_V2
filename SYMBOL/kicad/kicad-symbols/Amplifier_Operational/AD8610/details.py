
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "AD8610"
    hexID = "SZKAMPLIFIEROPERATIONALAD861"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM741', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AD8610', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/AD8610_8620.pdf', 'kicadSymbolki_keywords': 'single opamp', 'kicadSymbolki_description': 'Single Precision, Very Low Noise, Low Input Bias Current, Wide Bandwidth JFET Operational Amplifiers, SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm* DIP*W7.62mm* TSSOP*3x3mm*P0.65mm*'}])
    newPart['name'].append('Amplifier_Operational : AD8610')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

