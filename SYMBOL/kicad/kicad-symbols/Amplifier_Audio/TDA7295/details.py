
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Audio"
    oIndex = "TDA7295"
    hexID = "SZKAMPLIFIERAUDIOTDA7295"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TDA7293', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TDA7295', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-220-15_P2.54x2.54mm_StaggerOdd_Lead4.58mm_Vertical', 'kicadSymbolDatasheet': 'http://www.st.com/resource/en/datasheet/tda7295.pdf', 'kicadSymbolki_keywords': 'audio amplifier', 'kicadSymbolki_description': '80V - 80W DMOS Audio Amplifier with Mute/St-by, TO-220-15', 'kicadSymbolki_fp_filters': 'TO?220*StaggerOdd*'}])
    newPart['name'].append('Amplifier_Audio : TDA7295')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

