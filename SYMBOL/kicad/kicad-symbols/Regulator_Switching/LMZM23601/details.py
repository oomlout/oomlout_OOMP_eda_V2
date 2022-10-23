
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LMZM23601"
    hexID = "SZKREGULATORSWITCHINGLMZM2361"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LMZM23601', 'kicadSymbolFootprint': 'Package_LGA:Texas_SIL0010A_MicroSiP-10-1EP_3.8x3mm_P0.6mm_EP0.7x2.9mm_ThermalVias', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lmzm23601.pdf', 'kicadSymbolki_keywords': 'Step-Down DC/DC Module', 'kicadSymbolki_description': '1A Adjustable Step-Down DC/DC Power Module in 3.8x3mm, MicroSIP-10', 'kicadSymbolki_fp_filters': 'Texas*SIL*1EP*3.8x3mm*P0.6mm*'}])
    newPart['name'].append('LMZM23601')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

