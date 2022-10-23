
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Reference_Voltage"
    oIndex = "LT1634BCMS8-2.5"
    hexID = "SZKREFERENCEVOLTAGELT1634BCMS825"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LT1634BCMS8-1.25', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LT1634BCMS8-2.5', 'kicadSymbolFootprint': 'Package_SO:MSOP-8_3x3mm_P0.65mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/1634ff.pdf', 'kicadSymbolki_keywords': 'voltage reference Micropower', 'kicadSymbolki_description': '2.5V Micropower Precision Shunt Voltage Reference, MSOP-8', 'kicadSymbolki_fp_filters': 'MSOP?8*3x3mm*P0.65mm*'}])
    newPart['name'].append('LT1634BCMS8-2.5')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

