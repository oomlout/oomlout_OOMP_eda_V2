
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Audio"
    oIndex = "PAM8403D"
    hexID = "SZKAMPLIFIERAUDIOPAM843D"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PAM8403D', 'kicadSymbolFootprint': 'Package_SO:SOP-16_3.9x9.9mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.diodes.com/assets/Datasheets/PAM8403.pdf', 'kicadSymbolki_keywords': 'audio amplifier class d', 'kicadSymbolki_description': '3W Filterless Class-D Stereo Audio Amplifier, SOP-16', 'kicadSymbolki_fp_filters': 'SOP*3.9x9.9mm*P1.27mm*'}])
    newPart['name'].append('PAM8403D')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

