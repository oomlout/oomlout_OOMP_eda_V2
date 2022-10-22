
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "L272D"
    hexID = "SZKAMPLIFIEROPERATIONALL272D"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'L272D', 'kicadSymbolFootprint': 'Package_SO:SOIC-16_3.9x9.9mm_P1.27mm', 'kicadSymbolDatasheet': 'www.st.com/resource/en/datasheet/l272.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'dual power opamp', 'kicadSymbolki_description': 'Dual Power Operation Amplifier, SOIC-16', 'kicadSymbolki_fp_filters': '*SOIC*3.9x9.9mm*P1.27mm*'}])
    newPart['name'].append('L272D')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

