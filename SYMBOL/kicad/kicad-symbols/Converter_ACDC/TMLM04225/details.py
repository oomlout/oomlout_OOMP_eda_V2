
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Converter_ACDC"
    oIndex = "TMLM04225"
    hexID = "SZKCONTMLM4225"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'PS', 'kicadSymbolValue': 'TMLM04225', 'kicadSymbolFootprint': 'Converter_ACDC:Converter_ACDC_TRACO_TMLM-04_THT', 'kicadSymbolDatasheet': 'https://www.tracopower.com/products/tmlm.pdf', 'kicadSymbolki_keywords': 'Traco Power 4W AC-DC module power supply', 'kicadSymbolki_description': '12V 250mA / 5V 120mA AC/DC dual output, low noise power module', 'kicadSymbolki_fp_filters': 'Converter*ACDC*TRACO*TMLM*04*'}])
    newPart['name'].append('Converter_ACDC : TMLM04225')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

