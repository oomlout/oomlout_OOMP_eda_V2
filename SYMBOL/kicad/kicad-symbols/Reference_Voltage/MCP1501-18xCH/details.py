
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Reference_Voltage"
    oIndex = "MCP1501-18xCH"
    hexID = "SZKREFERENCEVOLTAGEMCP15118XCH"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MCP1501-10xCH', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP1501-18xCH', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-6', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/20005474E.pdf', 'kicadSymbolki_keywords': 'precision buffered voltage reference 1.8V', 'kicadSymbolki_description': '1.8V, 0.1%, 20mA, Precision Voltage Reference, SOT-23-6', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Reference_Voltage : MCP1501-18xCH')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

