
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_ADC"
    oIndex = "MAX11127xTI"
    hexID = "SZKANALOGADCMAX11127XTI"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MAX11126xTI', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX11127xTI', 'kicadSymbolFootprint': 'Package_DFN_QFN:TQFN-28-1EP_5x5mm_P0.5mm_EP3.25x3.25mm', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/MAX11120-MAX11128.pdf', 'kicadSymbolki_keywords': 'MAXIM ADC 3.3V 10-Bit SPI', 'kicadSymbolki_description': '16-Channel 10-Bit 1.5MHz Full-Linear Bandwidth External Reference High-Speed Low-Power ADC, QFN-28', 'kicadSymbolki_fp_filters': '*QFN*1EP*5x5mm*P0.5mm*'}])
    newPart['name'].append('MAX11127xTI')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

