
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Converter_ACDC"
    oIndex = "TMLM10124"
    hexID = "SZKCONTMLM1124"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TMLM10103', 'kicadSymbolReference': 'PS', 'kicadSymbolValue': 'TMLM10124', 'kicadSymbolFootprint': 'Converter_ACDC:Converter_ACDC_TRACO_TMLM-10-20_THT', 'kicadSymbolDatasheet': 'https://www.tracopower.com/products/tmlm.pdf', 'kicadSymbolki_keywords': 'Traco Power 10W AC-DC module power supply', 'kicadSymbolki_description': '24V 417mA AC/DC low noise power module', 'kicadSymbolki_fp_filters': 'Converter*ACDC*TRACO*TMLM*10*'}])
    newPart['name'].append('TMLM10124')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

