
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Temperature"
    oIndex = "PCT2075DP"
    hexID = "SZKSENTEMPERATUREPCT275DP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PCT2075DP', 'kicadSymbolFootprint': 'Package_SO:TSSOP-8_3x3mm_P0.65mm', 'kicadSymbolDatasheet': 'https://www.nxp.com/docs/en/data-sheet/PCT2075.pdf', 'kicadSymbolki_keywords': 'temperature sensor I2C single channel', 'kicadSymbolki_description': 'NXP I2C-bus Fm+ digital temperature sensor and thermal watchdog, TSSOP-8', 'kicadSymbolki_fp_filters': 'TSSOP*3x3mm*P0.65mm*'}])
    newPart['name'].append('Sensor_Temperature : PCT2075DP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

