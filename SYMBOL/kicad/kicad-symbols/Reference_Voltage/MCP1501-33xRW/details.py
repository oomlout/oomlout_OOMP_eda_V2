
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Reference_Voltage"
    oIndex = "MCP1501-33xRW"
    hexID = "SZKREFERENCEVOLTAGEMCP15133XRW"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MCP1501-10xRW', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP1501-33xRW', 'kicadSymbolFootprint': 'Package_DFN_QFN:WDFN-8-1EP_2x2mm_P0.5mm_EP0.8x1.2mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/20005474E.pdf', 'kicadSymbolki_keywords': 'precision buffered voltage reference 3.3V', 'kicadSymbolki_description': '3.3V, 0.1%, 20mA, Precision Voltage Reference, WDFN-8', 'kicadSymbolki_fp_filters': 'WDFN*1EP*2x2mm*P0.5mm*'}])
    newPart['name'].append('Reference_Voltage : MCP1501-33xRW')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

