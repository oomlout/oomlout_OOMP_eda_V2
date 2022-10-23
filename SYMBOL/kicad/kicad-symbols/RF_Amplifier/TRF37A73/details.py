
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Amplifier"
    oIndex = "TRF37A73"
    hexID = "SZKRFAMPLIFIERTRF37A73"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TRF37A73', 'kicadSymbolFootprint': 'Package_SON:WSON-8-1EP_2x2mm_P0.5mm_EP0.9x1.6mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/trf37a73.pdf', 'kicadSymbolki_keywords': 'gain block RF', 'kicadSymbolki_description': '6GHz, 12dB RF Gain Block, WSON-8', 'kicadSymbolki_fp_filters': 'WSON*1EP*2x2mm*P0.5mm*'}])
    newPart['name'].append('TRF37A73')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

