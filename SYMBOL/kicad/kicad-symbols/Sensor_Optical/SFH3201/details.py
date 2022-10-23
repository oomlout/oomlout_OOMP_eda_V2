
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Optical"
    oIndex = "SFH3201"
    hexID = "SZKSENOPTICALSFH321"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'SFH3201', 'kicadSymbolFootprint': 'OptoDevice:Osram_SFH9x0x', 'kicadSymbolDatasheet': 'https://dammedia.osram.info/media/resource/hires/osram-dam-2495980/SFH%203201.pdf', 'kicadSymbolki_keywords': 'NPN phototransistor', 'kicadSymbolki_description': 'Silicon NPN phototransistor, SMD-6', 'kicadSymbolki_fp_filters': 'Osram*SFH9x0x*'}])
    newPart['name'].append('SFH3201')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

