
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Optical"
    oIndex = "SFH203FA"
    hexID = "SZKSENOPTICALSFH23FA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SFH203', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'SFH203FA', 'kicadSymbolFootprint': 'LED_THT:LED_D5.0mm_IRGrey', 'kicadSymbolDatasheet': 'http://www.osram-os.com/Graphics/XPic9/00101656_0.pdf/SFH%20203,%20SFH%20203%20FA,%20Lead%20(Pb)%20Free%20Product%20-%20RoHS%20Compliant.pdf', 'kicadSymbolki_keywords': 'PIN photodiode IR', 'kicadSymbolki_description': 'Silicon PIN Photodiode with Daylight Blocking Filter', 'kicadSymbolki_fp_filters': 'LED*D5.0mm*IRGrey*'}])
    newPart['name'].append('Sensor_Optical : SFH203FA')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

