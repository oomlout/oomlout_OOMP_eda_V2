
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Audio"
    oIndex = "TPA6132A2RTE"
    hexID = "SZKAMPLIFIERAUDIOTPA6132A2RTE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPA6132A2RTE', 'kicadSymbolFootprint': 'Package_DFN_QFN:WQFN-16-1EP_3x3mm_P0.5mm_EP1.6x1.6mm_ThermalVias', 'kicadSymbolDatasheet': 'https://www.ti.com/lit/ds/symlink/tpa6132a2.pdf', 'kicadSymbolki_keywords': 'DirectPath audio amplifier Stereo', 'kicadSymbolki_description': '25mW, Stereo, DirectPath Audio Amplifier, WQFN-16', 'kicadSymbolki_fp_filters': 'WQFN*1EP*3x3mm*P0.5mm*'}])
    newPart['name'].append('TPA6132A2RTE')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

