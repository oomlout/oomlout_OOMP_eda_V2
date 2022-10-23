
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LT1584-ADJ"
    hexID = "SZKREGULATORLINEARLT1584ADJ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM350_TO220', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LT1584-ADJ', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-220-3_Vertical', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/158457a.pdf', 'kicadSymbolki_keywords': 'Voltage Regulator 7A Positive Adjustable', 'kicadSymbolki_description': 'Positive 7A 35V Low Dropout Fast Response Linear Regulator, Adjustable Output, TO-220', 'kicadSymbolki_fp_filters': 'TO?220*'}])
    newPart['name'].append('LT1584-ADJ')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

