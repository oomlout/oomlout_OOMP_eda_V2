
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LTC3630ADHC"
    hexID = "SZKREGULATORSWITCHINGLTC363ADHC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LTC3630DHC', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC3630ADHC', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-16-1EP_3x5mm_P0.5mm_EP1.66x4.4mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/3630afc.pdf', 'kicadSymbolki_keywords': 'buck dc-dc switcher switching', 'kicadSymbolki_description': 'High efficiency 76V 500mA synchronous step-down converter, DFN-16', 'kicadSymbolki_fp_filters': 'DFN*EP*3x5mm*P0.5mm*'}])
    newPart['name'].append('LTC3630ADHC')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

