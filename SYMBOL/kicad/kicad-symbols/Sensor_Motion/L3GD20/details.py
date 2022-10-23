
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Motion"
    oIndex = "L3GD20"
    hexID = "SZKSENMOTIONL3GD2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'L3GD20', 'kicadSymbolFootprint': 'Package_LGA:LGA-16_4x4mm_P0.65mm_LayoutBorder4x4y', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00036465.pdf', 'kicadSymbolki_keywords': '3-Axis MEMS Gyroscope', 'kicadSymbolki_description': '[Not recommended for new designs] 16-bit 3 Axis Digital MEMS Gyroscope, LGA-16', 'kicadSymbolki_fp_filters': 'LGA*4x4mm*P0.65mm*LayoutBorder4x4y*'}])
    newPart['name'].append('L3GD20')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

