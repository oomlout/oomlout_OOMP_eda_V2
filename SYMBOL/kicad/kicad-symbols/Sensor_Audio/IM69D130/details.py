
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Audio"
    oIndex = "IM69D130"
    hexID = "SZKSENAUDIOIM69D13"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'IM69D120', 'kicadSymbolReference': 'MK', 'kicadSymbolValue': 'IM69D130', 'kicadSymbolFootprint': 'Sensor_Audio:Infineon_PG-LLGA-5-1', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/Infineon-IM69D130-DS-v01_00-EN.pdf?fileId=5546d462602a9dc801607a0e46511a2e', 'kicadSymbolki_keywords': 'mems microphone', 'kicadSymbolki_description': 'High performance digital XENSIV MEMS microphone, -36 dBFS Sensitivity, LLGA-5', 'kicadSymbolki_fp_filters': 'Infineon*PG*LLGA*'}])
    newPart['name'].append('IM69D130')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

