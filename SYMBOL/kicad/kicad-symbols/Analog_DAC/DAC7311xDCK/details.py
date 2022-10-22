
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_DAC"
    oIndex = "DAC7311xDCK"
    hexID = "SZKANALOGDACDAC7311XDCK"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'DAC5311xDCK', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'DAC7311xDCK', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-363_SC-70-6', 'kicadSymbolDatasheet': 'https://www.ti.com/lit/ds/symlink/dac5311.pdf', 'kicadSymbolki_keywords': 'DAC SPI 1-channel', 'kicadSymbolki_description': '12-Bit, Single-Channel, Voltage Output, Serial Interface Digital-to-Analog Converters, SC-70', 'kicadSymbolki_fp_filters': 'SOT?363*'}])
    newPart['name'].append('DAC7311xDCK')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

