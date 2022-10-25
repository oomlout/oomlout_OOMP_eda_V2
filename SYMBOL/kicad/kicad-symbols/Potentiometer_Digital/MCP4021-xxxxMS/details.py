
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Potentiometer_Digital"
    oIndex = "MCP4021-xxxxMS"
    hexID = "SZKPOTENTIOMETERDIGITALMCP421XXXXMS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MCP4011-xxxxMS', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP4021-xxxxMS', 'kicadSymbolFootprint': 'Package_SO:MSOP-8_3x3mm_P0.65mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/21945e.pdf', 'kicadSymbolki_keywords': 'Digital Pot Potentiometer Up Down', 'kicadSymbolki_description': 'Low-Cost 64-Step Digital Potentiometer with WiperLock™ Technology, MSOP-8', 'kicadSymbolki_fp_filters': 'MSOP*3x3mm*P0.65mm*'}])
    newPart['name'].append('Potentiometer_Digital : MCP4021-xxxxMS')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

