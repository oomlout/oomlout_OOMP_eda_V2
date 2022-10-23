
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "LTV-352T"
    hexID = "SZKISOLATORLTV352T"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTV-352T', 'kicadSymbolFootprint': 'Package_SO:SO-4_4.4x3.6mm_P2.54mm', 'kicadSymbolDatasheet': 'http://optoelectronics.liteon.com/upload/download/DS70-2001-002/S_110_LTV-352T%2020140520.pdf', 'kicadSymbolki_keywords': 'NPN Darlington DC Optocoupler', 'kicadSymbolki_description': 'DC Darlington Optocoupler, Vce 300V, CTR 1000%, SO-4', 'kicadSymbolki_fp_filters': 'SO*4.4x3.6mm*P2.54mm*'}])
    newPart['name'].append('LTV-352T')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

