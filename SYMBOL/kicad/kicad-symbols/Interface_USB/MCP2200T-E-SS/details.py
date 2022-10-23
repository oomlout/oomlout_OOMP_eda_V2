
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_USB"
    oIndex = "MCP2200T-E-SS"
    hexID = "SZKINTERFACEUMCP22TESS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MCP2200-I-SS', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP2200T-E-SS', 'kicadSymbolFootprint': 'Package_SO:SSOP-20_5.3x7.2mm_P0.65mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/200022228D.pdf', 'kicadSymbolki_keywords': 'USB UART Converter', 'kicadSymbolki_description': 'USB 2.0 to UART Protocol Converter with GPIO, Extended Temperature Range, TnR, SSOP-20', 'kicadSymbolki_fp_filters': 'SSOP*20*5.3x7.2mm*P0.65mm*'}])
    newPart['name'].append('MCP2200T-E-SS')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

