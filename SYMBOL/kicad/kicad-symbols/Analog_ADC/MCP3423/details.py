
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_ADC"
    oIndex = "MCP3423"
    hexID = "SZKANALOGADCMCP3423"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP3423', 'kicadSymbolFootprint': 'Package_SO:MSOP-10_3x3mm_P0.5mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/22088c.pdf', 'kicadSymbolki_keywords': '18-Bit ADC I2C IIC I²C Delta-Sigma-ADC Delta-Sigma-ADC Reference 2ch', 'kicadSymbolki_description': '2-Channel, 18-Bit, Delta-Sigma AD-Converter, I²C Interface, Reference, MSOP', 'kicadSymbolki_fp_filters': 'MSOP*3x3mm*P0.5mm*'}])
    newPart['name'].append('Analog_ADC : MCP3423')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

