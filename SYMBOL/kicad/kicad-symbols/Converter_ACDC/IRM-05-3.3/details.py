
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Converter_ACDC"
    oIndex = "IRM-05-3.3"
    hexID = "SZKCONIRM533"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'PS', 'kicadSymbolValue': 'IRM-05-3.3', 'kicadSymbolFootprint': 'Converter_ACDC:Converter_ACDC_MeanWell_IRM-05-xx_THT', 'kicadSymbolDatasheet': 'https://www.meanwell.com/Upload/PDF/IRM-05/IRM-05-SPEC.PDF', 'kicadSymbolki_keywords': 'Miniature Module-type Power Supply MeanWell', 'kicadSymbolki_description': '3.3V, 1.25A, 4.125W, Isolated, AC-DC, 222A(IRM05)', 'kicadSymbolki_fp_filters': 'Converter*ACDC*MeanWell*IRM*05*THT*'}])
    newPart['name'].append('IRM-05-3.3')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

