
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Optical"
    oIndex = "SFH2400"
    hexID = "SZKSENOPTICALSFH24"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'SFH2400', 'kicadSymbolFootprint': 'OptoDevice:Osram_SMD-SmartDIL', 'kicadSymbolDatasheet': 'http://www.osram-os.com/Graphics/XPic5/00215665_0.pdf/SFH%202400.pdf', 'kicadSymbolki_keywords': 'opto photodiode', 'kicadSymbolki_description': 'Silicon PIN Photodiode, SMD package', 'kicadSymbolki_fp_filters': 'Osram*SMD*SmartDIL*'}])
    newPart['name'].append('SFH2400')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

