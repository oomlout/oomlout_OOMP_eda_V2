
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_DAC"
    oIndex = "MAX5217"
    hexID = "SZKANALOGDACMAX5217"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MAX5215', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX5217', 'kicadSymbolFootprint': 'Package_SO:MSOP-8_3x3mm_P0.65mm', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/MAX5215-MAX5217.pdf', 'kicadSymbolki_keywords': 'DA 16 Bit 1 ch', 'kicadSymbolki_description': 'Digital to analog, 16 Bit, 1 ch, 2.7 - 5.5 VDD, I2C, uMAX-8', 'kicadSymbolki_fp_filters': 'MSOP*3x3mm*P0.65mm*'}])
    newPart['name'].append('Analog_DAC : MAX5217')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

