
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Converter_ACDC"
    oIndex = "TMLM05112"
    hexID = "SZKCONTMLM5112"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TMLM05103', 'kicadSymbolReference': 'PS', 'kicadSymbolValue': 'TMLM05112', 'kicadSymbolFootprint': 'Converter_ACDC:Converter_ACDC_TRACO_TMLM-05_THT', 'kicadSymbolDatasheet': 'https://www.tracopower.com/products/tmlm.pdf', 'kicadSymbolki_keywords': 'Traco Power 5W AC-DC module power supply', 'kicadSymbolki_description': '12V 420mA AC/DC low noise power module', 'kicadSymbolki_fp_filters': 'Converter*ACDC*TRACO*TMLM*05*'}])
    newPart['name'].append('Converter_ACDC : TMLM05112')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

