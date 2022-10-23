
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "BDJ2GA5WEFJ"
    hexID = "SZKREGULATORLINEARBDJ2GA5WEFJ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BD15GA5WEFJ', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'BDJ2GA5WEFJ', 'kicadSymbolFootprint': 'Package_SO:HTSOP-8-1EP_3.9x4.9mm_P1.27mm_EP2.4x3.2mm', 'kicadSymbolDatasheet': 'http://rohmfs.rohm.com/en/products/databook/datasheet/ic/power/linear_regulator/bdxxga5wefj-e.pdf', 'kicadSymbolki_keywords': 'linear regulator fixed positive over voltage protection thermal shutdown', 'kicadSymbolki_description': '500mA, 12V LDO regulator with OVP & TSP, HTSOP-8', 'kicadSymbolki_fp_filters': 'HTSOP*1EP*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('BDJ2GA5WEFJ')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

