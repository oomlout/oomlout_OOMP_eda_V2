
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Proximity"
    oIndex = "TSSP58P38"
    hexID = "SZKSENPROXIMITYTSSP58P38"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TSSP58P38', 'kicadSymbolFootprint': 'OptoDevice:Vishay_MINICAST-3Pin', 'kicadSymbolDatasheet': 'http://www.vishay.com/docs/82462/tsop581.pdf', 'kicadSymbolki_keywords': 'opto IR receiver', 'kicadSymbolki_description': 'Photo Modules for PCM Remote Control Systems', 'kicadSymbolki_fp_filters': 'Vishay*MINICAST*'}])
    newPart['name'].append('TSSP58P38')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

