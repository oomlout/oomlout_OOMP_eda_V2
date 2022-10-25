
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface"
    oIndex = "AD9912"
    hexID = "SZKINTERFACEAD9912"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AD9912', 'kicadSymbolFootprint': 'Package_CSP:LFCSP-64-1EP_9x9mm_P0.5mm_EP5.21x5.21mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/ad9912.pdf', 'kicadSymbolki_keywords': 'Direct Digital Synthesizer DDS', 'kicadSymbolki_description': '1 GSPS, 14-bit DAC, Direct Digital Synthesizer, LFCSP-64', 'kicadSymbolki_fp_filters': 'LFCSP*1EP*9x9mm*P0.5mm*'}])
    newPart['name'].append('Interface : AD9912')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

