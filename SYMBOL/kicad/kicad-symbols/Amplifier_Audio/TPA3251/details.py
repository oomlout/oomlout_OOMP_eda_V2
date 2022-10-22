
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Audio"
    oIndex = "TPA3251"
    hexID = "SZKAMPLIFIERAUDIOTPA3251"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPA3251', 'kicadSymbolFootprint': 'Package_SO:HTSSOP-44_6.1x14mm_P0.635mm_TopEP4.14x7.01mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tpa3251.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'stereo class d amplifier', 'kicadSymbolki_description': '175-W Stereo, 350-W Mono PurePath Ultra-HD Analog-Input Class-D Amplifier, HTSSOP-44', 'kicadSymbolki_fp_filters': 'HTSSOP*6.1x14mm*P0.635mm*'}])
    newPart['name'].append('TPA3251')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

