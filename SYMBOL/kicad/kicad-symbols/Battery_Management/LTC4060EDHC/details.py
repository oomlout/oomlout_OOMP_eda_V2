
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Battery_Management"
    oIndex = "LTC4060EDHC"
    hexID = "SZKBATMANAGEMENTLTC46EDHC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC4060EDHC', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-16-1EP_3x5mm_P0.5mm_EP1.66x4.4mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/405442xf.pdf', 'kicadSymbolki_keywords': 'Complete fast charging system for 2, 3 or 4 series NiMH or NiCd batteries, 0.4 to 2A, 4.5 to 10V VDD, -40 to +85 degree Celcisus, DFN-16', 'kicadSymbolki_description': 'Complete fast charging system for 2, 3 or 4 series  NiMH or NiCd batteries, 0.4 to 2A, 4.5 to 10V VDD, -40 to +85 degree Celcisus, DFN-16', 'kicadSymbolki_fp_filters': 'DFN*1EP*3x5mm*P0.5mm*'}])
    newPart['name'].append('LTC4060EDHC')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

