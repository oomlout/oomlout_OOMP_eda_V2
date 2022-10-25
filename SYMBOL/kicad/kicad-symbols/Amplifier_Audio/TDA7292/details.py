
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Audio"
    oIndex = "TDA7292"
    hexID = "SZKAMPLIFIERAUDIOTDA7292"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TDA7265', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TDA7292', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-220-11_P3.4x5.08mm_StaggerOdd_Lead4.85mm_Vertical', 'kicadSymbolDatasheet': 'http://www.st.com/resource/en/datasheet/tda7292.pdf', 'kicadSymbolki_keywords': 'audio amplifier 2ch', 'kicadSymbolki_description': '40W + 40W stereo amplifier with mute and standby, TO-220-11', 'kicadSymbolki_fp_filters': 'TO?220*StaggerOdd*'}])
    newPart['name'].append('Amplifier_Audio : TDA7292')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

