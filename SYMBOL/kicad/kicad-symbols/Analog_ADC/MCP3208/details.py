
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_ADC"
    oIndex = "MCP3208"
    hexID = "SZKANALOGADCMCP328"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP3208', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/21298c.pdf', 'kicadSymbolki_keywords': '12bit ADC Reference Single Supply SPI 8ch', 'kicadSymbolki_description': 'A/D Converter, 12-Bit, 8-Channel, SPI Interface , 2.7V-5.5V', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* SOIC*3.9x9.9mm*P1.27mm*'}])
    newPart['name'].append('Analog_ADC : MCP3208')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

