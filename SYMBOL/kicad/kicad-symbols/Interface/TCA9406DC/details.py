
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface"
    oIndex = "TCA9406DC"
    hexID = "SZKINTERFACETCA946DC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TCA9406DC', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'www.ti.com/lit/ds/symlink/tca9406.pdf', 'kicadSymbolki_keywords': 'Bidirectional 1-MHz I2C SMBus Voltage-Level Translator 8kV HBM ESD', 'kicadSymbolki_description': '2-Bit Bidirectional 1-MHz, I2C Bus and SMBus Voltage-Level Translator With 8-kV HBM ESD', 'kicadSymbolki_fp_filters': 'SSOP*2.95x2.8mm*P0.65mm* VSSOP*2.3x2mm*P0.5mm*'}])
    newPart['name'].append('Interface : TCA9406DC')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

