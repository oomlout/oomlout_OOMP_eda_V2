
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Optical"
    oIndex = "SFH2430"
    hexID = "SZKSENOPTICALSFH243"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BP104-SMD', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'SFH2430', 'kicadSymbolFootprint': 'OptoDevice:Osram_SFH2430', 'kicadSymbolDatasheet': 'https://dammedia.osram.info/media/resource/hires/osram-dam-5467144/SFH%202430_EN.pdf', 'kicadSymbolki_keywords': 'opto photodiode', 'kicadSymbolki_description': 'Silicon Photodiode, Vf 1.2V, Area 2.65x2.65mm', 'kicadSymbolki_fp_filters': 'Osram*SFH2430*'}])
    newPart['name'].append('SFH2430')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

