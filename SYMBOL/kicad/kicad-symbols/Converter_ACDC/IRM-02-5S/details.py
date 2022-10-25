
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Converter_ACDC"
    oIndex = "IRM-02-5S"
    hexID = "SZKCONIRM25S"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'IRM-02-3.3S', 'kicadSymbolReference': 'PS', 'kicadSymbolValue': 'IRM-02-5S', 'kicadSymbolFootprint': 'Converter_ACDC:Converter_ACDC_MeanWell_IRM-02-xx_SMD', 'kicadSymbolDatasheet': 'https://www.meanwell.com/Upload/PDF/IRM-02/IRM-02-SPEC.PDF', 'kicadSymbolki_keywords': 'Miniature Module-type Power Supply MeanWell', 'kicadSymbolki_description': '5V, 400mA, 2W, Isolated, AC-DC, IRM02-SMD', 'kicadSymbolki_fp_filters': 'Converter*ACDC*MeanWell*IRM*02*SMD*'}])
    newPart['name'].append('Converter_ACDC : IRM-02-5S')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

