
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor"
    oIndex = "BL0937"
    hexID = "SZKSENBL937"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'BL0937', 'kicadSymbolFootprint': 'Package_SO:SOP-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'http://www.belling.com.cn/media/file_object/bel_product/BL0937/datasheet/BL0937_V1.02_en.pdf', 'kicadSymbolki_keywords': 'current sensor', 'kicadSymbolki_description': 'Single Phase Energy Meter IC with Integrated Oscillator, SOP-8', 'kicadSymbolki_fp_filters': 'SOP*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('BL0937')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

