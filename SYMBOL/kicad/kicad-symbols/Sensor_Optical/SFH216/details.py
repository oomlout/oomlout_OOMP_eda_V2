
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Optical"
    oIndex = "SFH216"
    hexID = "SZKSENOPTICALSFH216"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'SFH216', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-18-2_Window', 'kicadSymbolDatasheet': 'http://www.osram-os.com/Graphics/XPic1/00029253_0.pdf/SFH', 'kicadSymbolki_keywords': 'opto PIN photo diode', 'kicadSymbolki_description': 'Silicon PIN Photodiode With Very Short Switching Time, TO-18 package', 'kicadSymbolki_fp_filters': 'TO?18*Window*'}])
    newPart['name'].append('SFH216')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

