
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface"
    oIndex = "TCA9800"
    hexID = "SZKINTERFACETCA98"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TCA9800', 'kicadSymbolFootprint': 'Package_SO:VSSOP-8_3.0x3.0mm_P0.65mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tca9800.pdf', 'kicadSymbolki_keywords': 'I2C buffer repeater', 'kicadSymbolki_description': 'Level-Translating I2C Bus Buffer/Repeater 0.54mA Current Source, VSSOP-8', 'kicadSymbolki_fp_filters': 'VSSOP*3.0x3.0mm*P0.65mm*'}])
    newPart['name'].append('Interface : TCA9800')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

