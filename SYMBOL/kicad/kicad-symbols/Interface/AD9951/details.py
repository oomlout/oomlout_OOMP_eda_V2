
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface"
    oIndex = "AD9951"
    hexID = "SZKINTERFACEAD9951"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AD9951', 'kicadSymbolFootprint': 'Package_QFP:TQFP-48-1EP_7x7mm_P0.5mm_EP3.5x3.5mm', 'kicadSymbolDatasheet': 'https://www.analog.com/static/imported-files/data_sheets/AD9951.pdf', 'kicadSymbolki_keywords': 'Direct Digital Synthesizer DDS', 'kicadSymbolki_description': '14-Bit Direct Digital Synthesizer with 400MSPS DAC, 1.8V, TQFP48', 'kicadSymbolki_fp_filters': 'TQFP*1EP*7x7mm*P0.5mm*'}])
    newPart['name'].append('AD9951')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

