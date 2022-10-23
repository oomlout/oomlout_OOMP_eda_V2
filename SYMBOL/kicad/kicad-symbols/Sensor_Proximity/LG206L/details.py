
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Proximity"
    oIndex = "LG206L"
    hexID = "SZKSENPROXIMITYLG26L"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LG206L', 'kicadSymbolFootprint': 'OptoDevice:Kodenshi_LG206L', 'kicadSymbolDatasheet': 'http://kodenshi.co.jp/products/pdf/sensor/photointerrupter_ic/LG206L.pdf', 'kicadSymbolki_keywords': 'Photointerrupter infrared LED with photo IC, inverting output, -0.5V to 17V VDD, -20 to +85 degree Celsius, LG206X', 'kicadSymbolki_description': 'Photointerrupter infrared LED with photo IC, inverting output, -0.5V to 17V VDD, -20 to +85 degree Celsius, LG206X', 'kicadSymbolki_fp_filters': 'Kodenshi?LG206L*'}])
    newPart['name'].append('LG206L')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

