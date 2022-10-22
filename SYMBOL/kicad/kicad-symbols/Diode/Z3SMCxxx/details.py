
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "Z3SMCxxx"
    hexID = "SZKDIODEZ3SMCXXX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ZPYxx', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'Z3SMCxxx', 'kicadSymbolFootprint': 'Diode_SMD:D_SMC', 'kicadSymbolDatasheet': 'https://diotec.com/tl_files/diotec/files/pdf/datasheets/z3smc1.pdf', 'kicadSymbolki_keywords': 'zener diode', 'kicadSymbolki_description': '3000mW Zener Diode, SMC(DO-214AB)', 'kicadSymbolki_fp_filters': 'D?SMC*'}])
    newPart['name'].append('Z3SMCxxx')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

