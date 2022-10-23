
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Optical"
    oIndex = "SFH203"
    hexID = "SZKSENOPTICALSFH23"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'SFH203', 'kicadSymbolFootprint': 'LED_THT:LED_D5.0mm_IRGrey', 'kicadSymbolDatasheet': 'http://www.osram-os.com/Graphics/XPic9/00101656_0.pdf/SFH%20203,%20SFH%20203%20FA,%20Lead%20(Pb)%20Free%20Product%20-%20RoHS%20Compliant.pdf', 'kicadSymbolki_keywords': 'opto PIN photodiode', 'kicadSymbolki_description': 'Silicon PIN Photodiode', 'kicadSymbolki_fp_filters': 'LED*D5.0mm*IRGrey*'}])
    newPart['name'].append('SFH203')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

