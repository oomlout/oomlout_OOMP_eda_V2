
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Battery_Management"
    oIndex = "LTC4060EFE"
    hexID = "SZKBATMANAGEMENTLTC46EFE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC4060EFE', 'kicadSymbolFootprint': 'Package_SO:TSSOP-16-1EP_4.4x5mm_P0.65mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/405442xf.pdf', 'kicadSymbolki_keywords': 'Complete fast charging system for 2, 3 or 4 series NiMH or NiCd batteries, 0.4 to 2A, 4.5 to 10V VDD, -40 to +85 degree Celcisus, TSSOP-16', 'kicadSymbolki_description': 'Complete fast charging system for 2, 3 or 4 series NiMH or NiCd batteries, 0.4 to 2A, 4.5 to 10V VDD, -40 to +85 degree Celcisus, TSSOP-16', 'kicadSymbolki_fp_filters': 'TSSOP*EP*4.4x5mm*P0.65mm*'}])
    newPart['name'].append('LTC4060EFE')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

