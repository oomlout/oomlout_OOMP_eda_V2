
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Optical"
    oIndex = "BPW34-SMD"
    hexID = "SZKSENOPTICALBPW34SM"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BP104-SMD', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'BPW34-SMD', 'kicadSymbolFootprint': 'OptoDevice:Osram_BPW34S-SMD', 'kicadSymbolDatasheet': 'https://dammedia.osram.info/media/resource/hires/osram-dam-5488319/BPW%2034%20S_EN.pdf', 'kicadSymbolki_keywords': 'opto photodiode', 'kicadSymbolki_description': 'Silicon PIN Photodiode, Area 2.65x2.65mm', 'kicadSymbolki_fp_filters': 'Osram*BPW34S*'}])
    newPart['name'].append('BPW34-SMD')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

