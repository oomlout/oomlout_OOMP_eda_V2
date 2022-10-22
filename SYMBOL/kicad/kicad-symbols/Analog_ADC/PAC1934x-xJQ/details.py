
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_ADC"
    oIndex = "PAC1934x-xJQ"
    hexID = "SZKANALOGADCPAC1934XXJQ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PAC1934x-xJQ', 'kicadSymbolFootprint': 'Package_DFN_QFN:UQFN-16-1EP_4x4mm_P0.65mm_EP2.7x2.7mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/PAC1931-Family-Data-Sheet-DS20005850E.pdf', 'kicadSymbolki_keywords': 'I2C Current Shunt Energy Monitor', 'kicadSymbolki_description': 'Multi-Channel DC Power/Energy Monitor with Accumulator, UQFN-16', 'kicadSymbolki_fp_filters': 'UQFN*1EP*4x4mm*P0.65mm*'}])
    newPart['name'].append('PAC1934x-xJQ')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

