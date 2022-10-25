
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "LED"
    oIndex = "SFH4346"
    hexID = "SZKLSFH4346"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SFH4356P', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'SFH4346', 'kicadSymbolFootprint': 'LED_THT:LED_D3.0mm_IRBlack', 'kicadSymbolDatasheet': 'http://cdn-reichelt.de/documents/datenblatt/A500/SFH4346.pdf', 'kicadSymbolki_keywords': 'opto IR LED', 'kicadSymbolki_description': 'Infrared LED , 3mm LED package', 'kicadSymbolki_fp_filters': 'LED*3.0mm*IRBlack*'}])
    newPart['name'].append('LED : SFH4346')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

