
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Optical"
    oIndex = "SFH225FA"
    hexID = "SZKSENOPTICALSFH225FA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'SFH225FA', 'kicadSymbolFootprint': 'OptoDevice:Osram_SFH225', 'kicadSymbolDatasheet': 'http://www.osram-os.com/Graphics/XPic0/00209685_0.pdf/SFH%20225%20FA.pdf', 'kicadSymbolki_keywords': 'opto PIN photodiode IR', 'kicadSymbolki_description': 'Silicon PIN Photodiode with Daylight Blocking Filter', 'kicadSymbolki_fp_filters': 'Osram*SFH225*'}])
    newPart['name'].append('SFH225FA')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

