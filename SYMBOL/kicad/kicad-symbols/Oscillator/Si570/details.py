
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Oscillator"
    oIndex = "Si570"
    hexID = "SZKOCSSI57"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'Si570', 'kicadSymbolFootprint': 'Oscillator:Oscillator_SMD_SI570_SI571_Standard', 'kicadSymbolDatasheet': 'http://www.silabs.com/Support%20Documents/TechnicalDocs/si570.pdf', 'kicadSymbolki_keywords': '10 MHZ TO 1.4 GHZ I2C PROGRAMMABLE XO/VCXO', 'kicadSymbolki_description': '10 MHZ TO 1.4 GHZ I2C PROGRAMMABLE XO/VCXO', 'kicadSymbolki_fp_filters': 'Oscillator*SI570*SI571*'}])
    newPart['name'].append('Oscillator : Si570')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

