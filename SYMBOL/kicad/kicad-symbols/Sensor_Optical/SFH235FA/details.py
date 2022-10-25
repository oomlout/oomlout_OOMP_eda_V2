
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Optical"
    oIndex = "SFH235FA"
    hexID = "SZKSENOPTICALSFH235FA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SFH225FA', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'SFH235FA', 'kicadSymbolFootprint': 'OptoDevice:Osram_SFH225', 'kicadSymbolDatasheet': 'http://www.osram-os.com/Graphics/XPic3/00211469_0.pdf/SFH%20235%20FA.pdf', 'kicadSymbolki_keywords': 'opto PIN photodiode IR', 'kicadSymbolki_description': 'Silicon PIN Photodiode with Daylight Blocking Filter', 'kicadSymbolki_fp_filters': 'Osram*SFH225*'}])
    newPart['name'].append('Sensor_Optical : SFH235FA')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

