
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Converter_ACDC"
    oIndex = "TMLM04112"
    hexID = "SZKCONTMLM4112"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TMLM04103', 'kicadSymbolReference': 'PS', 'kicadSymbolValue': 'TMLM04112', 'kicadSymbolFootprint': 'Converter_ACDC:Converter_ACDC_TRACO_TMLM-04_THT', 'kicadSymbolDatasheet': 'https://www.tracopower.com/products/tmlm.pdf', 'kicadSymbolki_keywords': 'Traco Power 4W AC-DC module power supply', 'kicadSymbolki_description': '12V 333mA AC/DC low noise power module', 'kicadSymbolki_fp_filters': 'Converter*ACDC*TRACO*TMLM*04*'}])
    newPart['name'].append('TMLM04112')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

