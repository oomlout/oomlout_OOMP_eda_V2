
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Converter_ACDC"
    oIndex = "IRM-20-24"
    hexID = "SZKCONIRM224"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'IRM-20-3.3', 'kicadSymbolReference': 'PS', 'kicadSymbolValue': 'IRM-20-24', 'kicadSymbolFootprint': 'Converter_ACDC:Converter_ACDC_MeanWell_IRM-20-xx_THT', 'kicadSymbolDatasheet': 'http://www.meanwell.com/Upload/PDF/IRM-20/IRM-20-SPEC.PDF', 'kicadSymbolki_keywords': 'Miniature Module-type Power Supply MeanWell', 'kicadSymbolki_description': '24V, 900mA, 21.6W, Isolated, AC-DC, 219A(IRM20)', 'kicadSymbolki_fp_filters': 'Converter*ACDC*MeanWell*IRM*20*THT*'}])
    newPart['name'].append('IRM-20-24')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

