
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Audio"
    oIndex = "TDA7266D"
    hexID = "SZKAMPLIFIERAUDIOTDA7266D"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TDA7266D', 'kicadSymbolFootprint': 'Package_SO:HSOP-20-1EP_11.0x15.9mm_P1.27mm_SlugDown', 'kicadSymbolDatasheet': 'http://www.st.com/resource/en/datasheet/tda7266d.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'audio amplifier 2ch', 'kicadSymbolki_description': '5W+5W Dual Bridge Amplifier, PowerSO-20', 'kicadSymbolki_fp_filters': 'HSOP*EP*11.0x15.9mm*P1.27mm*SlugDown*'}])
    newPart['name'].append('Amplifier_Audio : TDA7266D')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

