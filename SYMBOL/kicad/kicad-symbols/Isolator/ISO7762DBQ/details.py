
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "ISO7762DBQ"
    hexID = "SZKISOLATORISO7762DBQ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ISO7762DBQ', 'kicadSymbolFootprint': 'Package_SO:SSOP-16_3.9x4.9mm_P0.635mm', 'kicadSymbolDatasheet': 'https://www.ti.com/lit/ds/symlink/iso7763.pdf', 'kicadSymbolki_keywords': '6 channel digital isolator', 'kicadSymbolki_description': 'Default high, High-speed, robust EMC, reinforced, six-channel, digital, isolator, SSOP-16', 'kicadSymbolki_fp_filters': 'SSOP*3.9x4.9mm*P0.635mm*'}])
    newPart['name'].append('ISO7762DBQ')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

