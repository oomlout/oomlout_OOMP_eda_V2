
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_Expansion"
    oIndex = "AS1115-BSST"
    hexID = "SZKINTERFACEEXPANSIONAS1115BSST"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AS1115-BSST', 'kicadSymbolFootprint': 'Package_SO:QSOP-24_3.9x8.7mm_P0.635mm', 'kicadSymbolDatasheet': 'https://ams.com/documents/20143/36005/AS1115_DS000206_1-00.pdf/3d3e6d35-b184-1329-adf9-2d769eb2404f', 'kicadSymbolki_keywords': 'led driver i2c', 'kicadSymbolki_description': '64 LEDs, I2C Interfaced LED Driver with Keyscan, QSOP-24', 'kicadSymbolki_fp_filters': 'QSOP*3.9x8.7m*P0.635mm*'}])
    newPart['name'].append('Interface_Expansion : AS1115-BSST')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

