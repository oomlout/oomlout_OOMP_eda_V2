
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Converter_ACDC"
    oIndex = "PBO-3-S9"
    hexID = "SZKCONPBO3S9"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PBO-3-S3.3', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PBO-3-S9', 'kicadSymbolFootprint': 'Converter_ACDC:Converter_ACDC_CUI_PBO-3-Sxx_THT_Vertical', 'kicadSymbolDatasheet': 'https://www.cui.com/product/resource/pbo-3.pdf', 'kicadSymbolki_keywords': 'ac dc power supply', 'kicadSymbolki_description': '9V 0.333A 3W miniature AC-DC module-type power supply', 'kicadSymbolki_fp_filters': 'Converter*ACDC*CUI*PBO*3*Sxx*THT*'}])
    newPart['name'].append('Converter_ACDC : PBO-3-S9')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

