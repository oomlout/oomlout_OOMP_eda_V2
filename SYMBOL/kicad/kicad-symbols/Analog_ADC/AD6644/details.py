
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_ADC"
    oIndex = "AD6644"
    hexID = "SZKANALOGADCAD6644"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AD6644', 'kicadSymbolFootprint': 'Package_QFP:TQFP-52-1EP_10x10mm_P0.65mm_EP6.5x6.5mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/AD6644.pdf', 'kicadSymbolki_keywords': 'ADC differential analog digital converter', 'kicadSymbolki_description': 'A/D Converter, 14-Bit, 40 MSPS/65 MSPS, TQFP-52', 'kicadSymbolki_fp_filters': 'TQFP*1EP*10x10mm*P0.65mm*'}])
    newPart['name'].append('AD6644')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

