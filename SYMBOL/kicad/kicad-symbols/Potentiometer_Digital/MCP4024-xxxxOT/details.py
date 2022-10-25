
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Potentiometer_Digital"
    oIndex = "MCP4024-xxxxOT"
    hexID = "SZKPOTENTIOMETERDIGITALMCP424XXXXOT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MCP4014-xxxxOT', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP4024-xxxxOT', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-5', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/21945e.pdf', 'kicadSymbolki_keywords': 'Digital Pot Potentiometer Up Down', 'kicadSymbolki_description': 'Low-Cost 64-Step Digital Potentiometer with WiperLock™ Technology, SOT-23-5', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Potentiometer_Digital : MCP4024-xxxxOT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

