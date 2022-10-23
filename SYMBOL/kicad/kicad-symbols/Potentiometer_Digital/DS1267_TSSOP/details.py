
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Potentiometer_Digital"
    oIndex = "DS1267_TSSOP"
    hexID = "SZKPOTENTIOMETERDIGITALDS1267TSS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'DS1267_TSSOP', 'kicadSymbolFootprint': 'Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/DS1267.pdf', 'kicadSymbolki_keywords': 'Dual Digital Potentiometer Maxim', 'kicadSymbolki_description': 'Dual Digital Potentiometer, Serial, 256 Steps, TSSOP-20', 'kicadSymbolki_fp_filters': 'TSSOP*4.4x6.5mm*0.65mm*'}])
    newPart['name'].append('DS1267_TSSOP')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

