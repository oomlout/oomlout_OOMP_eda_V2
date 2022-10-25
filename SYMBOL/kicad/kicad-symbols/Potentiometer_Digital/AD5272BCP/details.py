
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Potentiometer_Digital"
    oIndex = "AD5272BCP"
    hexID = "SZKPOTENTIOMETERDIGITALAD5272BCP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AD5272BCP', 'kicadSymbolFootprint': 'Package_CSP:LFCSP-WD-10-1EP_3x3mm_P0.5mm_EP1.64x2.38mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/AD5272_5274.pdf', 'kicadSymbolki_keywords': 'digital potentiometer', 'kicadSymbolki_description': 'Digital potentiometer, 1024 position, 1% Resistor Tolerance, I2C interface, LFCSP-10', 'kicadSymbolki_fp_filters': 'LFCSP*1EP*3x3mm*P0.5mm*'}])
    newPart['name'].append('Potentiometer_Digital : AD5272BCP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

