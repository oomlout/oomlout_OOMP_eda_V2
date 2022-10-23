
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Magnetic"
    oIndex = "AS5050A"
    hexID = "SZKSENMAGNETICAS55A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AS5055A', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AS5050A', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-16-1EP_4x4mm_P0.65mm_EP2.7x2.7mm_PullBack', 'kicadSymbolDatasheet': 'https://ams.com/documents/20143/36005/AS5055A_DS000304_2-00.pdf', 'kicadSymbolki_keywords': 'sensor magnetic hall position rotation spi', 'kicadSymbolki_description': 'Magnetic position sensor, 10-bit, SPI interface, QFN-16', 'kicadSymbolki_fp_filters': 'QFN*1EP*4x4mm*P0.65mm*PullBack*'}])
    newPart['name'].append('AS5050A')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

