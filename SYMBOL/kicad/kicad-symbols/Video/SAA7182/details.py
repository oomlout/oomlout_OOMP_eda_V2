
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Video"
    oIndex = "SAA7182"
    hexID = "SZKVIDEOSAA7182"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SAA7182', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://rcl-radio.ru/wp-content/uploads/2014/11/SAA7182.pdf', 'kicadSymbolki_keywords': 'Video Encoder', 'kicadSymbolki_description': 'Digital Video Encoder, Obsolete'}])
    newPart['name'].append('Video : SAA7182')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

