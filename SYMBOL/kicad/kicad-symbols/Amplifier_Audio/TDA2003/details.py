
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Audio"
    oIndex = "TDA2003"
    hexID = "SZKAMPLIFIERAUDIOTDA23"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TDA2003', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-220-5_P3.4x3.7mm_StaggerOdd_Lead3.8mm_Vertical', 'kicadSymbolDatasheet': 'http://www.st.com/resource/en/datasheet/cd00000123.pdf', 'kicadSymbolki_keywords': 'audio amplifier', 'kicadSymbolki_description': '10W Car Radio Audio Amplifier, TO-220-5', 'kicadSymbolki_fp_filters': 'TO*220*StaggerOdd*'}])
    newPart['name'].append('Amplifier_Audio : TDA2003')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

