
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "DSP_AnalogDevices"
    oIndex = "ADAU1450"
    hexID = "SZKDSPANALOGDEVICESADAU145"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADAU1450', 'kicadSymbolFootprint': 'Package_CSP:LFCSP-72-1EP_10x10mm_P0.5mm_EP5.3x5.3mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/ADAU1452_1451_1450.pdf', 'kicadSymbolki_keywords': 'sigmadsp audio', 'kicadSymbolki_description': 'SigmaDSP SigmaDSP Digital Audio Processor, 147.456 MHz, 8kword Data RAM, I2C/SPI, LFCSP-72', 'kicadSymbolki_fp_filters': 'LFCSP*1EP*10x10mm*P0.5mm*'}])
    newPart['name'].append('ADAU1450')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

