
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_Expansion"
    oIndex = "MAX7325AEG+"
    hexID = "SZKINTERFACEEXPANSIONMAX7325AEG+"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX7325AEG+', 'kicadSymbolFootprint': 'Package_SO:QSOP-24_3.9x8.7mm_P0.635mm', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/MAX7325.pdf', 'kicadSymbolki_keywords': 'Expander I2C Parallel Port GPIO Maxim', 'kicadSymbolki_description': 'I2C Port Expander with 8 Push-Pull and 8 Open-Drain I/Os, QSOP-24', 'kicadSymbolki_fp_filters': 'QSOP*3.9x8.7*P0.635mm*'}])
    newPart['name'].append('MAX7325AEG+')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

