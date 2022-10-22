
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_FET"
    oIndex = "FAN3278"
    hexID = "SZKDRIVERFETFAN3278"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'FAN3268', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'FAN3278', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/FAN3278-D.pdf', 'kicadSymbolki_keywords': 'Driver MOSFET', 'kicadSymbolki_description': '8-27V PMOS-NMOS Bridge Driver, SOIC-8', 'kicadSymbolki_fp_filters': '*SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('FAN3278')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

