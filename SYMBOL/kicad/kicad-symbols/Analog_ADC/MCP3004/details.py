
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_ADC"
    oIndex = "MCP3004"
    hexID = "SZKANALOGADCMCP34"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP3004', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/21295C.pdf', 'kicadSymbolki_keywords': '10-Bit ADC SPI 4CH', 'kicadSymbolki_description': '4-Channel 10-Bit A/D Converters with SPI Interface', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* SOIC*3.9x8.7mm*P1.27mm* TSSOP*4.4x5mm*P0.65mm*'}])
    newPart['name'].append('Analog_ADC : MCP3004')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

