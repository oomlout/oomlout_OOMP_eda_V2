
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Audio"
    oIndex = "TDA7266M"
    hexID = "SZKAMPLIFIERAUDIOTDA7266M"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TDA7266M', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-220-15_P2.54x2.54mm_StaggerOdd_Lead4.58mm_Vertical', 'kicadSymbolDatasheet': 'http://www.st.com/resource/en/datasheet/tda7266m.pdf', 'kicadSymbolki_keywords': 'audio amplifier', 'kicadSymbolki_description': '7W Mono Bridge Amplifier, TO-220-15', 'kicadSymbolki_fp_filters': 'TO?220*StaggerOdd*'}])
    newPart['name'].append('Amplifier_Audio : TDA7266M')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

