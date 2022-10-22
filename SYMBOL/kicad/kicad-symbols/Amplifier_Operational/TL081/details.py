
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "TL081"
    hexID = "SZKAMPLIFIEROPERATIONALTL81"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM741', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TL081', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tl081.pdf', 'kicadSymbolki_keywords': 'single opamp', 'kicadSymbolki_description': 'Single JFET-Input Operational Amplifiers, DIP-8/SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm* DIP*W7.62mm* TSSOP*3x3mm*P0.65mm*'}])
    newPart['name'].append('TL081')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

