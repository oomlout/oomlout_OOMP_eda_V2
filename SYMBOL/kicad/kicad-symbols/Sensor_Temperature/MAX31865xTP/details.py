
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Temperature"
    oIndex = "MAX31865xTP"
    hexID = "SZKSENTEMPERATUREMAX31865XTP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX31865xTP', 'kicadSymbolFootprint': 'Package_DFN_QFN:TQFN-20-1EP_5x5mm_P0.65mm_EP3.25x3.25mm', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/MAX31865.pdf', 'kicadSymbolki_keywords': 'RTD SPI Temperature', 'kicadSymbolki_description': 'RTD-to-Digital Converter, TQFN-20', 'kicadSymbolki_fp_filters': 'TQFN*1EP*5x5mm*P0.65mm*'}])
    newPart['name'].append('MAX31865xTP')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

