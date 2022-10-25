
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Optical"
    oIndex = "SFH2440"
    hexID = "SZKSENOPTICALSFH244"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BP104-SMD', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'SFH2440', 'kicadSymbolFootprint': 'OptoDevice:Osram_SFH2440', 'kicadSymbolDatasheet': 'https://dammedia.osram.info/media/resource/hires/osram-dam-5467146/SFH%202440_EN.pdf', 'kicadSymbolki_keywords': 'opto photodiode', 'kicadSymbolki_description': 'Silicon Photodiode, Vf 1V, Area 2.65x2.65mm', 'kicadSymbolki_fp_filters': 'Osram*SFH2440*'}])
    newPart['name'].append('Sensor_Optical : SFH2440')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

