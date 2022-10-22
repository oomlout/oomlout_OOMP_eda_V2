
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Audio"
    oIndex = "LM4990MH"
    hexID = "SZKAMPLIFIERAUDIOLM499MH"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM4990MH', 'kicadSymbolFootprint': 'Package_SO:MSOP-10-1EP_3x3mm_P0.5mm_EP1.68x1.88mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm4990.pdf', 'kicadSymbolki_keywords': 'audio amplifier class d', 'kicadSymbolki_description': 'Boomer 2 Watt Audio Power Amplifier with Selectable Shutdown Logic Level, MSOP-10', 'kicadSymbolki_fp_filters': 'MSOP*EP*3x3mm*P0.5mm*'}])
    newPart['name'].append('LM4990MH')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

