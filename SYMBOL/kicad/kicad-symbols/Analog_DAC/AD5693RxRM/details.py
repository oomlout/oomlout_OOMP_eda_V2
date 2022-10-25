
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_DAC"
    oIndex = "AD5693RxRM"
    hexID = "SZKANALOGDACAD5693RXRM"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AD5691RxRM', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AD5693RxRM', 'kicadSymbolFootprint': 'Package_SO:MSOP-10_3x3mm_P0.5mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/AD5693R_5692R_5691R_5693.pdf', 'kicadSymbolki_keywords': 'serial DAC i2c digital analog converter', 'kicadSymbolki_description': 'Tiny, 16-Bit, I2C, nanoDAC+, 2 ppm/°C Reference, MSOP-10', 'kicadSymbolki_fp_filters': 'MSOP*3x3mm*P0.5mm*'}])
    newPart['name'].append('Analog_DAC : AD5693RxRM')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

