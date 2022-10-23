
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_Expansion"
    oIndex = "MCP23008-xSO"
    hexID = "SZKINTERFACEEXPANSIONMCP238XSO"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP23008-xSO', 'kicadSymbolFootprint': 'Package_SO:SOIC-18W_7.5x11.6mm_P1.27mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/MCP23008-MCP23S08-Data-Sheet-20001919F.pdf', 'kicadSymbolki_keywords': 'I2C parallel port expander', 'kicadSymbolki_description': '8-bit I/O expander, I2C, interrupts, SOIC-18', 'kicadSymbolki_fp_filters': 'SOIC*7.5x11.6mm*P1.27mm*'}])
    newPart['name'].append('MCP23008-xSO')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

