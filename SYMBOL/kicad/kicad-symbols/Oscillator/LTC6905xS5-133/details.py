
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Oscillator"
    oIndex = "LTC6905xS5-133"
    hexID = "SZKOCSLTC695XS5133"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LTC6905xS5-80', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC6905xS5-133', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TSOT-23-5', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/6905xfa.pdf', 'kicadSymbolki_keywords': 'oscillator fixed frequency divider silicon', 'kicadSymbolki_description': '2.7-5.5V 133MHz Precision Fixed Frequency Silicon Oscillator, TSOT-23-5', 'kicadSymbolki_fp_filters': 'TSOT?23?5*'}])
    newPart['name'].append('Oscillator : LTC6905xS5-133')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

