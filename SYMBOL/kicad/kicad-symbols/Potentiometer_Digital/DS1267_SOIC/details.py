
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Potentiometer_Digital"
    oIndex = "DS1267_SOIC"
    hexID = "SZKPOTENTIOMETERDIGITALDS1267SOIC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'DS1267_SOIC', 'kicadSymbolFootprint': 'Package_SO:SOIC-16_3.9x9.9mm_P1.27mm', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/DS1267.pdf', 'kicadSymbolki_keywords': 'Dual Digital Potentiometer Maxim', 'kicadSymbolki_description': 'Dual Digital Potentiometer, Serial, 256 Steps, SOIC-16', 'kicadSymbolki_fp_filters': 'SOIC*3.9x9.9mm*1.27mm*'}])
    newPart['name'].append('Potentiometer_Digital : DS1267_SOIC')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

