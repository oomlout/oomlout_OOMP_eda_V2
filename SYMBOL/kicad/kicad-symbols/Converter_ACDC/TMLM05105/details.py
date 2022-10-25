
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Converter_ACDC"
    oIndex = "TMLM05105"
    hexID = "SZKCONTMLM515"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TMLM05103', 'kicadSymbolReference': 'PS', 'kicadSymbolValue': 'TMLM05105', 'kicadSymbolFootprint': 'Converter_ACDC:Converter_ACDC_TRACO_TMLM-05_THT', 'kicadSymbolDatasheet': 'https://www.tracopower.com/products/tmlm.pdf', 'kicadSymbolki_keywords': 'Traco Power 5W AC-DC module power supply', 'kicadSymbolki_description': '5V 1000mA AC/DC low noise power module', 'kicadSymbolki_fp_filters': 'Converter*ACDC*TRACO*TMLM*05*'}])
    newPart['name'].append('Converter_ACDC : TMLM05105')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

