
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Reference_Voltage"
    oIndex = "MCP1501-10xRW"
    hexID = "SZKREFERENCEVOLTAGEMCP1511XRW"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP1501-10xRW', 'kicadSymbolFootprint': 'Package_DFN_QFN:WDFN-8-1EP_2x2mm_P0.5mm_EP0.8x1.2mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/20005474E.pdf', 'kicadSymbolki_keywords': 'precision buffered voltage reference 1.024V', 'kicadSymbolki_description': '1.024V, 0.1%, 20mA, Precision Voltage Reference, WDFN-8', 'kicadSymbolki_fp_filters': 'WDFN*1EP*2x2mm*P0.5mm*'}])
    newPart['name'].append('MCP1501-10xRW')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

