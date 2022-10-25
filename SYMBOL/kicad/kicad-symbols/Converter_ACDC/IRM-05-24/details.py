
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Converter_ACDC"
    oIndex = "IRM-05-24"
    hexID = "SZKCONIRM524"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'IRM-05-3.3', 'kicadSymbolReference': 'PS', 'kicadSymbolValue': 'IRM-05-24', 'kicadSymbolFootprint': 'Converter_ACDC:Converter_ACDC_MeanWell_IRM-05-xx_THT', 'kicadSymbolDatasheet': 'https://www.meanwell.com/Upload/PDF/IRM-05/IRM-05-SPEC.PDF', 'kicadSymbolki_keywords': 'Miniature Module-type Power Supply MeanWell', 'kicadSymbolki_description': '24V, 230mA, 5.52W, Isolated, AC-DC, 222A(IRM05)', 'kicadSymbolki_fp_filters': 'Converter*ACDC*MeanWell*IRM*05*THT*'}])
    newPart['name'].append('Converter_ACDC : IRM-05-24')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

