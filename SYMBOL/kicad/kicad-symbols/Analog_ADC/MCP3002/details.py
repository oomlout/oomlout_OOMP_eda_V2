
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_ADC"
    oIndex = "MCP3002"
    hexID = "SZKANALOGADCMCP32"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP3002', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/21294E.pdf', 'kicadSymbolki_keywords': 'Dual Channel 10-Bit ADC SPI 2CH', 'kicadSymbolki_description': 'Dual Channel 10-Bit A/D Converter with SPI Serial Interface', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm** SOIC*3.9x4.9mm*P1.27mm* TSSOP*3x3mm*P0.65mm* MSOP*3x3mm*P0.65mm*'}])
    newPart['name'].append('Analog_ADC : MCP3002')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

