
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Potentiometer_Digital"
    oIndex = "MCP4021-xxxxSN"
    hexID = "SZKPOTENTIOMETERDIGITALMCP421XXXXSN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MCP4011-xxxxSN', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP4021-xxxxSN', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/21945e.pdf', 'kicadSymbolki_keywords': 'Digital Pot Potentiometer Up Down', 'kicadSymbolki_description': 'Low-Cost 64-Step Digital Potentiometer with WiperLock™ Technology, SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Potentiometer_Digital : MCP4021-xxxxSN')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

