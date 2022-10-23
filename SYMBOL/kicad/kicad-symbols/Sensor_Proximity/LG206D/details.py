
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Proximity"
    oIndex = "LG206D"
    hexID = "SZKSENPROXIMITYLG26D"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LG206D', 'kicadSymbolFootprint': 'OptoDevice:Kodenshi_LG206D', 'kicadSymbolDatasheet': 'http://kodenshi.co.jp/products/pdf/sensor/photointerrupter_ic/LG206D.pdf', 'kicadSymbolki_keywords': 'Photointerrupter infrared LED with photo IC, non-inverting output, -0.5V to 17V VDD, -20 to +85 degree Celsius, LG206D', 'kicadSymbolki_description': 'Photointerrupter infrared LED with photo IC, non-inverting output, -0.5V to 17V VDD, -20 to +85 degree Celsius, LG206D', 'kicadSymbolki_fp_filters': 'Kodenshi?LG206D*'}])
    newPart['name'].append('LG206D')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

