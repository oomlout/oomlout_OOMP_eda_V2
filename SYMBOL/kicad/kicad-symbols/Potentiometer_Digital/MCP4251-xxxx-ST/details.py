
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Potentiometer_Digital"
    oIndex = "MCP4251-xxxx-ST"
    hexID = "SZKPOTENTIOMETERDIGITALMCP4251XXXXST"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP4251-xxxx-ST', 'kicadSymbolFootprint': 'Package_SO:TSSOP-14_4.4x5mm_P0.65mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/devicedoc/22060b.pdf', 'kicadSymbolki_keywords': 'Digital Pot Potentiometer', 'kicadSymbolki_description': 'Dual 8 Bit Digital Pot, SPI, Volatile Memory, TSSOP-14', 'kicadSymbolki_fp_filters': 'TSSOP*4.4x5mm*P0.65mm*'}])
    newPart['name'].append('Potentiometer_Digital : MCP4251-xxxx-ST')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

