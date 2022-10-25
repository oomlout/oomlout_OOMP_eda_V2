
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Potentiometer_Digital"
    oIndex = "MCP45HV31-ST"
    hexID = "SZKPOTENTIOMETERDIGITALMCP45HV31ST"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MCP45HV51-ST', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP45HV31-ST', 'kicadSymbolFootprint': 'Package_SO:TSSOP-14_4.4x5mm_P0.65mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/20005304A.pdf', 'kicadSymbolki_keywords': 'I2C Potentiometer pot digital', 'kicadSymbolki_description': '7/8-bit single +36V (+/-18V) digital pot, I2C serial interface, volatile memory, TSSOP-14', 'kicadSymbolki_fp_filters': 'TSSOP*4.4x5mm*P0.65mm*'}])
    newPart['name'].append('Potentiometer_Digital : MCP45HV31-ST')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

