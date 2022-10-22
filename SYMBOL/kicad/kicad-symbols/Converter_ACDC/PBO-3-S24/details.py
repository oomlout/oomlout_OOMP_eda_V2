
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Converter_ACDC"
    oIndex = "PBO-3-S24"
    hexID = "SZKCONPBO3S24"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PBO-3-S3.3', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PBO-3-S24', 'kicadSymbolFootprint': 'Converter_ACDC:Converter_ACDC_CUI_PBO-3-Sxx_THT_Vertical', 'kicadSymbolDatasheet': 'https://www.cui.com/product/resource/pbo-3.pdf', 'kicadSymbolki_keywords': 'ac dc power supply', 'kicadSymbolki_description': '24V 0.125A 3W miniature AC-DC module-type power supply', 'kicadSymbolki_fp_filters': 'Converter*ACDC*CUI*PBO*3*Sxx*THT*'}])
    newPart['name'].append('PBO-3-S24')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

