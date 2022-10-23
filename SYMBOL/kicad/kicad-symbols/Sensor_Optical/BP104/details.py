
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Optical"
    oIndex = "BP104"
    hexID = "SZKSENOPTICALBP14"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BPW34', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'BP104', 'kicadSymbolFootprint': 'OptoDevice:Osram_DIL2_4.3x4.65mm_P5.08mm', 'kicadSymbolDatasheet': 'http://www.vishay.com/docs/81500/81500.pdf', 'kicadSymbolki_keywords': 'opto PIN photodiode', 'kicadSymbolki_description': 'Silicon PIN Photodiode', 'kicadSymbolki_fp_filters': 'Osram*DIL2*4.3x4.65mm*P5.08*'}])
    newPart['name'].append('BP104')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

