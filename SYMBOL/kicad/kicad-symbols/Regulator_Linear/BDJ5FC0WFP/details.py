
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "BDJ5FC0WFP"
    hexID = "SZKREGULATORLINEARBDJ5FCWFP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BD30FC0WFP', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'BDJ5FC0WFP', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-252-4', 'kicadSymbolDatasheet': 'https://fscdn.rohm.com/en/products/databook/datasheet/ic/power/linear_regulator/bdxxfc0wefj-e.pdf', 'kicadSymbolki_keywords': 'linear regulator fixed positive over voltage protection thermal shutdown', 'kicadSymbolki_description': '1A, 15.0V LDO regulator with OVP & TSP, with enable, TO-252', 'kicadSymbolki_fp_filters': 'TO?252*'}])
    newPart['name'].append('BDJ5FC0WFP')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

