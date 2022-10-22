
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_ADC"
    oIndex = "ADS7868"
    hexID = "SZKANALOGADCADS7868"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ADS7866', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADS7868', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TSOT-23-6', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/ads7866.pdf', 'kicadSymbolki_keywords': 'ADC', 'kicadSymbolki_description': 'Single Channel 8-bit ADC,  100-200ksps, SPI, micro-power, SOT-23-6', 'kicadSymbolki_fp_filters': '*SOT?23?6*'}])
    newPart['name'].append('ADS7868')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

