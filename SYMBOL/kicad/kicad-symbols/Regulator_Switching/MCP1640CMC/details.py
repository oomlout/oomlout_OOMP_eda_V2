
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "MCP1640CMC"
    hexID = "SZKREGULATORSWITCHINGMCP164CMC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MCP1640MC', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP1640CMC', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-8-1EP_3x2mm_P0.5mm_EP1.75x1.45mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/20002234D.pdf', 'kicadSymbolki_keywords': 'Step-Up Boost DC-DC Regulator Adjustable', 'kicadSymbolki_description': 'Synchronous Boost Regulator, Adjustable Output 2.0V-5.5V, PWM/PFM Input to Output Bypass, DFN-8', 'kicadSymbolki_fp_filters': 'DFN*1EP*3x2mm*P0.5mm*'}])
    newPart['name'].append('Regulator_Switching : MCP1640CMC')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

