
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Audio"
    oIndex = "TDA7266P"
    hexID = "SZKAMPLIFIERAUDIOTDA7266P"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TDA7266P', 'kicadSymbolFootprint': 'Package_SO:ST_PowerSSO-24_SlugDown', 'kicadSymbolDatasheet': 'http://www.st.com/resource/en/datasheet/tda7266p.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'audio amplifier 2ch', 'kicadSymbolki_description': '3W+3W Dual Bridge Amplifier, PowerSSO-24', 'kicadSymbolki_fp_filters': 'ST*PowerSSO*SlugDown*'}])
    newPart['name'].append('TDA7266P')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

