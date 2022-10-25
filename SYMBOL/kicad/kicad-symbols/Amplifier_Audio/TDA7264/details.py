
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Audio"
    oIndex = "TDA7264"
    hexID = "SZKAMPLIFIERAUDIOTDA7264"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TDA7264', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-220-8_Vertical', 'kicadSymbolDatasheet': 'http://www.st.com/resource/en/datasheet/tda7264.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'audio amplifier 2ch', 'kicadSymbolki_description': '25W + 25W stereo amplifier with mute and standby, TO-220-8', 'kicadSymbolki_fp_filters': 'TO?220*'}])
    newPart['name'].append('Amplifier_Audio : TDA7264')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

