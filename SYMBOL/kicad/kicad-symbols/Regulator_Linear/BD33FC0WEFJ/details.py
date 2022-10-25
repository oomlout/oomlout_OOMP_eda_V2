
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "BD33FC0WEFJ"
    hexID = "SZKREGULATORLINEARBD33FCWEFJ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BD30FC0WEFJ', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'BD33FC0WEFJ', 'kicadSymbolFootprint': 'Package_SO:HTSOP-8-1EP_3.9x4.9mm_P1.27mm_EP2.4x3.2mm', 'kicadSymbolDatasheet': 'https://fscdn.rohm.com/en/products/databook/datasheet/ic/power/linear_regulator/bdxxfc0wefj-e.pdf', 'kicadSymbolki_keywords': 'linear regulator fixed positive over voltage protection thermal shutdown', 'kicadSymbolki_description': '1A, 3.3V LDO regulator with OVP & TSP, with enable, HTSOP-J8', 'kicadSymbolki_fp_filters': 'HTSOP*1EP*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Regulator_Linear : BD33FC0WEFJ')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

