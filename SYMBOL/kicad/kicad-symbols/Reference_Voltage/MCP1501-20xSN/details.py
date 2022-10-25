
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Reference_Voltage"
    oIndex = "MCP1501-20xSN"
    hexID = "SZKREFERENCEVOLTAGEMCP1512XSN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MCP1501-10xSN', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP1501-20xSN', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/20005474E.pdf', 'kicadSymbolki_keywords': 'precision buffered voltage reference 2.048V', 'kicadSymbolki_description': '2.048V, 0.1%, 20mA, Precision Voltage Reference, SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Reference_Voltage : MCP1501-20xSN')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

