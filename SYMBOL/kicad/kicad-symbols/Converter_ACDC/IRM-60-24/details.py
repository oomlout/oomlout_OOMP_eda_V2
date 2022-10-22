
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Converter_ACDC"
    oIndex = "IRM-60-24"
    hexID = "SZKCONIRM624"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'IRM-60-5', 'kicadSymbolReference': 'PS', 'kicadSymbolValue': 'IRM-60-24', 'kicadSymbolFootprint': 'Converter_ACDC:Converter_ACDC_MeanWell_IRM-60-xx_THT', 'kicadSymbolDatasheet': 'http://www.meanwellusa.com/productPdf.aspx?i=687', 'kicadSymbolki_keywords': 'Miniature Module-type Power Supply MeanWell', 'kicadSymbolki_description': '24V, 2.5A, 60W, Isolated, AC-DC, IRM60', 'kicadSymbolki_fp_filters': 'Converter*ACDC*MeanWell*IRM*60*THT*'}])
    newPart['name'].append('IRM-60-24')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

