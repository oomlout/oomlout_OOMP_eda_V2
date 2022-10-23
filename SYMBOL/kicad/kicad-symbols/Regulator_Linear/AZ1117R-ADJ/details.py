
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "AZ1117R-ADJ"
    hexID = "SZKREGULATORLINEARAZ1117RADJ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM317L_SOT-89', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AZ1117R-ADJ', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-89-3', 'kicadSymbolDatasheet': 'https://www.diodes.com/assets/Datasheets/products_inactive_data/AZ1117.pdf', 'kicadSymbolki_keywords': 'Adjustable Voltage Regulator 1A Positive LDO', 'kicadSymbolki_description': '1A 20V Adjustable LDO Linear Regulator, SOT-89', 'kicadSymbolki_fp_filters': 'SOT?89*'}])
    newPart['name'].append('AZ1117R-ADJ')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

