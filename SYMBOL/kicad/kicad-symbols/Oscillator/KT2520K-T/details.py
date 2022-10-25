
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Oscillator"
    oIndex = "KT2520K-T"
    hexID = "SZKOCSKT252KT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'KT2520K-T', 'kicadSymbolFootprint': 'Oscillator:Oscillator_SMD_Kyocera_2520-6Pin_2.5x2.0mm', 'kicadSymbolDatasheet': 'https://global.kyocera.com/prdct/electro/product/pdf/kt2520_e.pdf', 'kicadSymbolki_keywords': 'tcxo', 'kicadSymbolki_description': '10-60MHz Temperature Compensated Crystal Oscillator, Kyocera 2520', 'kicadSymbolki_fp_filters': 'Oscillator*SMD*Kyocera*2.5x2.0mm*'}])
    newPart['name'].append('Oscillator : KT2520K-T')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

