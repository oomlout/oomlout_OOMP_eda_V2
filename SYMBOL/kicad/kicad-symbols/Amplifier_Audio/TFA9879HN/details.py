
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Audio"
    oIndex = "TFA9879HN"
    hexID = "SZKAMPLIFIERAUDIOTFA9879HN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TFA9879HN', 'kicadSymbolFootprint': 'Package_DFN_QFN:HVQFN-24-1EP_4x4mm_P0.5mm_EP2.6x2.6mm_ThermalVias', 'kicadSymbolDatasheet': 'https://www.nxp.com/docs/en/data-sheet/TFA9879.pdf', 'kicadSymbolki_keywords': 'Audio Amplifier Class D NXP Semiconductors', 'kicadSymbolki_description': 'Mono BTL class-D audio amplifier for portable applications with digital input, HVQFN-24', 'kicadSymbolki_fp_filters': 'HVQFN*1EP*4x4mm*P0.5mm*'}])
    newPart['name'].append('TFA9879HN')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

