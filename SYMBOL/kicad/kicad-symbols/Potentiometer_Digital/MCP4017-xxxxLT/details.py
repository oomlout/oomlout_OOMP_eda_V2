
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Potentiometer_Digital"
    oIndex = "MCP4017-xxxxLT"
    hexID = "SZKPOTENTIOMETERDIGITALMCP417XXXXLT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP4017-xxxxLT', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-363_SC-70-6', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/22147a.pdf', 'kicadSymbolki_keywords': 'TWI pot rheostat', 'kicadSymbolki_description': 'Low-Cost 128-Step Volatile I2C Digital Potentiometer, SC-70-6', 'kicadSymbolki_fp_filters': '*SC?70*'}])
    newPart['name'].append('Potentiometer_Digital : MCP4017-xxxxLT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

