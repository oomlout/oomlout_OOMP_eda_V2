
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Potentiometer_Digital"
    oIndex = "AD5253"
    hexID = "SZKPOTENTIOMETERDIGITALAD5253"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AD5254', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AD5253', 'kicadSymbolFootprint': 'Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/AD5253_5254.pdf', 'kicadSymbolki_keywords': 'digital potentiometer', 'kicadSymbolki_description': 'Digital potentiometer, 64 position, 4 output, I2C interface, TSSOP-20', 'kicadSymbolki_fp_filters': 'TSSOP*4.4x6.5mm*P0.65mm*'}])
    newPart['name'].append('Potentiometer_Digital : AD5253')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

