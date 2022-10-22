
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Audio"
    oIndex = "TDA2050"
    hexID = "SZKAMPLIFIERAUDIOTDA25"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TDA2030', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TDA2050', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-220-5_P3.4x3.7mm_StaggerOdd_Lead3.8mm_Vertical', 'kicadSymbolDatasheet': 'http://www.st.com/resource/en/datasheet/cd00000131.pdf', 'kicadSymbolki_keywords': 'audio amplifier', 'kicadSymbolki_description': '32W Hi-Fi Audio Amplifier, TO-220-5', 'kicadSymbolki_fp_filters': 'TO*220*StaggerOdd*'}])
    newPart['name'].append('TDA2050')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

