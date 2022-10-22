
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Converter_ACDC"
    oIndex = "IRM-03-12"
    hexID = "SZKCONIRM312"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'IRM-03-3.3', 'kicadSymbolReference': 'PS', 'kicadSymbolValue': 'IRM-03-12', 'kicadSymbolFootprint': 'Converter_ACDC:Converter_ACDC_MeanWell_IRM-03-xx_THT', 'kicadSymbolDatasheet': 'https://www.meanwell.com/Upload/PDF/IRM-03/IRM-03-SPEC.PDF', 'kicadSymbolki_keywords': 'Miniature Module-type Power Supply MeanWell', 'kicadSymbolki_description': '12V, 250mA, 3W, Isolated, AC-DC, IRM03', 'kicadSymbolki_fp_filters': 'Converter*ACDC*MeanWell*IRM*03*THT*'}])
    newPart['name'].append('IRM-03-12')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

