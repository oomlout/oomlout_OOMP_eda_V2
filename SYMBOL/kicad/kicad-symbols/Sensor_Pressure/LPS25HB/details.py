
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Pressure"
    oIndex = "LPS25HB"
    hexID = "SZKSENPRESSURELPS25HB"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LPS25HB', 'kicadSymbolFootprint': 'Package_LGA:ST_HLGA-10_2.5x2.5mm_P0.6mm_LayoutBorder3x2y', 'kicadSymbolDatasheet': 'www.st.com/resource/en/datasheet/lps25hb.pdf', 'kicadSymbolki_keywords': 'mems absolute baromeeter', 'kicadSymbolki_description': 'MEMS pressure sensor, 260-1260 hPa, absolute digital output baromeeter', 'kicadSymbolki_fp_filters': 'ST?HLGA*2.5x2.5mm*P0.6mm*LayoutBorder3x2y*'}])
    newPart['name'].append('LPS25HB')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

