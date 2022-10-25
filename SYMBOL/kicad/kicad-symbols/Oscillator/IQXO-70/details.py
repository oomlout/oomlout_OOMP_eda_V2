
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Oscillator"
    oIndex = "IQXO-70"
    hexID = "SZKOCSIQXO7"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'X', 'kicadSymbolValue': 'IQXO-70', 'kicadSymbolFootprint': 'Oscillator:Oscillator_SMD_IQD_IQXO70-4Pin_7.5x5.0mm', 'kicadSymbolDatasheet': 'http://www.iqdfrequencyproducts.com/products/details/iqxo-70-11-30.pdf', 'kicadSymbolki_keywords': 'Crystal Clock Oscillator', 'kicadSymbolki_description': 'Crystal Clock Oscillator, SMD package 7.5x5.0mm²', 'kicadSymbolki_fp_filters': 'Oscillator*SMD*IQD*IQXO70*7.5x5.0mm*'}])
    newPart['name'].append('Oscillator : IQXO-70')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

