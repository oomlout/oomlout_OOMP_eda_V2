
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Optical"
    oIndex = "BP104-SMD"
    hexID = "SZKSENOPTICALBP14SM"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'BP104-SMD', 'kicadSymbolFootprint': 'OptoDevice:Osram_BP104-SMD', 'kicadSymbolDatasheet': 'https://dammedia.osram.info/media/resource/hires/osram-dam-5989350/BP%20104%20FAS_EN.pdf', 'kicadSymbolki_keywords': 'opto photodiode', 'kicadSymbolki_description': 'Silicon PIN Photodiode,  Area 2.2x2.2mm', 'kicadSymbolki_fp_filters': 'Osram*BP104*'}])
    newPart['name'].append('BP104-SMD')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

