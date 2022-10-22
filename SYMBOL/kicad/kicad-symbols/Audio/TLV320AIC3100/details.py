
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Audio"
    oIndex = "TLV320AIC3100"
    hexID = "SZKAUDIOTLV32AIC31"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TLV320AIC3100', 'kicadSymbolFootprint': 'Package_DFN_QFN:VQFN-32-1EP_5x5mm_P0.5mm_EP3.5x3.5mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tlv320aic3100.pdf', 'kicadSymbolki_keywords': 'audio codec 2ch 192kHz class-d amplifier', 'kicadSymbolki_description': 'Low Power Audio Codec with Audio Processing and Mono Class‑D Amplifier, VQFN-32', 'kicadSymbolki_fp_filters': 'VQFN*1EP*5x5mm*P0.5mm*'}])
    newPart['name'].append('TLV320AIC3100')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

