
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_UART"
    oIndex = "ISL3283ExHZ"
    hexID = "SZKINTERFACEUARTISL3283EXHZ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ISL3283ExHZ', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-6', 'kicadSymbolDatasheet': 'https://www.renesas.com/us/en/www/doc/datasheet/isl3280e-81e-82e-83e-84e-85e.pdf', 'kicadSymbolki_keywords': 'Interface Driver Receiver Transceiver', 'kicadSymbolki_description': 'RS485, RS422, 20Mbps Transceiver, 3.0V to 5.5V, SOT-23-6', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Interface_UART : ISL3283ExHZ')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

