
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "LED"
    oIndex = "SFH482"
    hexID = "SZKLSFH482"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'SFH482', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-18-2_Window', 'kicadSymbolDatasheet': 'http://www.osram-os.com/Graphics/XPic2/00182155_0.pdf/SFH%20482%20E7800,%20Lead%20(Pb)%20Free%20Product%20-%20RoHS%20Compliant.pdf', 'kicadSymbolki_keywords': 'opto IR LED', 'kicadSymbolki_description': 'GaAlAs Infrared LED (880 nm), TO-18 package', 'kicadSymbolki_fp_filters': 'TO?18*Window*'}])
    newPart['name'].append('SFH482')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

