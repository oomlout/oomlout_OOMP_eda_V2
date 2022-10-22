
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "LM101"
    hexID = "SZKAMPLIFIEROPERATIONALLM11"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'NE5534', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM101', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm101a-n.pdf', 'kicadSymbolki_keywords': 'single opamp', 'kicadSymbolki_description': 'Operational Amplifier, DIP-8/TO-99-8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* SOIC*3.9x4.9mm*P1.27mm* TO?5*'}])
    newPart['name'].append('LM101')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

