
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "FODM217C"
    hexID = "SZKISOLATORFODM217C"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'FODM217A', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'FODM217C', 'kicadSymbolFootprint': 'Package_SO:SOP-4_4.4x2.6mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/FODM214-D.PDF', 'kicadSymbolki_keywords': 'DC Phototransistor Optocoupler', 'kicadSymbolki_description': 'DC Optocoupler, Vce 80V, CTR 200-400%, SOP-4', 'kicadSymbolki_fp_filters': 'SOP*4.4x2.6mm*P1.27mm*'}])
    newPart['name'].append('FODM217C')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

