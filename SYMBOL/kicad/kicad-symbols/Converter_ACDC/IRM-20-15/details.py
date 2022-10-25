
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Converter_ACDC"
    oIndex = "IRM-20-15"
    hexID = "SZKCONIRM215"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'IRM-20-3.3', 'kicadSymbolReference': 'PS', 'kicadSymbolValue': 'IRM-20-15', 'kicadSymbolFootprint': 'Converter_ACDC:Converter_ACDC_MeanWell_IRM-20-xx_THT', 'kicadSymbolDatasheet': 'http://www.meanwell.com/Upload/PDF/IRM-20/IRM-20-SPEC.PDF', 'kicadSymbolki_keywords': 'Miniature Module-type Power Supply MeanWell', 'kicadSymbolki_description': '15V, 1.4A, 21W, Isolated, AC-DC, 219A(IRM20)', 'kicadSymbolki_fp_filters': 'Converter*ACDC*MeanWell*IRM*20*THT*'}])
    newPart['name'].append('Converter_ACDC : IRM-20-15')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

