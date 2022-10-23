
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Optical"
    oIndex = "SFH206K"
    hexID = "SZKSENOPTICALSFH26K"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'SFH206K', 'kicadSymbolFootprint': 'OptoDevice:Osram_SFH205', 'kicadSymbolDatasheet': 'http://www.osram-os.com/Graphics/XPic0/00211439_0.pdf/SFH%20206%20K.pdf', 'kicadSymbolki_keywords': 'opto PIN photodiode', 'kicadSymbolki_description': 'Silicon PIN Photodiode', 'kicadSymbolki_fp_filters': 'Osram*SFH205*'}])
    newPart['name'].append('SFH206K')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

