
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Converter_ACDC"
    oIndex = "IRM-03-5"
    hexID = "SZKCONIRM35"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'IRM-03-3.3', 'kicadSymbolReference': 'PS', 'kicadSymbolValue': 'IRM-03-5', 'kicadSymbolFootprint': 'Converter_ACDC:Converter_ACDC_MeanWell_IRM-03-xx_THT', 'kicadSymbolDatasheet': 'https://www.meanwell.com/Upload/PDF/IRM-03/IRM-03-SPEC.PDF', 'kicadSymbolki_keywords': 'Miniature Module-type Power Supply MeanWell', 'kicadSymbolki_description': '5V, 600mA, 3W, Isolated, AC-DC, IRM03', 'kicadSymbolki_fp_filters': 'Converter*ACDC*MeanWell*IRM*03*THT*'}])
    newPart['name'].append('Converter_ACDC : IRM-03-5')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

