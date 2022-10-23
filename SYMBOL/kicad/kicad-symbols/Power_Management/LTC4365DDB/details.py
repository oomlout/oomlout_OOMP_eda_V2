
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Management"
    oIndex = "LTC4365DDB"
    hexID = "SZKPOWERMANAGEMENTLTC4365DDB"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC4365DDB', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-8-1EP_2x3mm_P0.5mm_EP0.61x2.2mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/4365fa.pdf', 'kicadSymbolki_keywords': 'overvoltage undervoltage reverse-polarity protection', 'kicadSymbolki_description': 'Overvoltage, Undervoltage and Reverse Supply Protection Controller, 3x2mm DFN-8 package, 50Hz/60Hz noise rejection', 'kicadSymbolki_fp_filters': 'DFN*1EP*2x3mm*P0.5mm*'}])
    newPart['name'].append('LTC4365DDB')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

