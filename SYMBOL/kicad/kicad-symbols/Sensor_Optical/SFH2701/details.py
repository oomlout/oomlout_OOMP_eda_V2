
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Optical"
    oIndex = "SFH2701"
    hexID = "SZKSENOPTICALSFH271"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'SFH2701', 'kicadSymbolFootprint': 'LED_SMD:LED_1206_3216Metric_Castellated', 'kicadSymbolDatasheet': 'http://www.osram-os.com/Graphics/XPic6/00201111_0.pdf/SFH%202701.pdf', 'kicadSymbolki_keywords': 'opto photodiode', 'kicadSymbolki_description': 'High Speed PIN Photodiode, SMD package', 'kicadSymbolki_fp_filters': 'LED*1206*'}])
    newPart['name'].append('SFH2701')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

