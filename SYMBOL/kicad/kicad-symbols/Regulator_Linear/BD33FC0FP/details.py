
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "BD33FC0FP"
    hexID = "SZKREGULATORLINEARBD33FCFP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'BD33FC0FP', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-252-2', 'kicadSymbolDatasheet': 'https://fscdn.rohm.com/en/products/databook/datasheet/ic/power/linear_regulator/bdxxfc0wefj-e.pdf', 'kicadSymbolki_keywords': 'linear regulator fixed positive over voltage protection thermal shutdown', 'kicadSymbolki_description': '1A, 3.3V LDO regulator with OVP & TSP, without enable, TO-252', 'kicadSymbolki_fp_filters': 'TO?252*'}])
    newPart['name'].append('Regulator_Linear : BD33FC0FP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

