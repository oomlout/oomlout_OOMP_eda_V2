
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "DSP_Microchip_DSPIC33"
    oIndex = "DSPIC33FJ64MC204"
    hexID = "SZKDSPMCHIPDSPIC33DSPIC33FJ64MC24"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'DSPIC33FJ64MC204', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/70291G.pdf', 'kicadSymbolki_keywords': '16-bit Digital Signal Controller Microchip dsPIC Motor Control', 'kicadSymbolki_description': '40MIPS, 64k Flash, 8k SRAM', 'kicadSymbolki_fp_filters': 'QFN?44*1EP*8x8mm*P0.65mm* TQFP?44*10x10mm*P0.8mm*'}])
    newPart['name'].append('DSPIC33FJ64MC204')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

