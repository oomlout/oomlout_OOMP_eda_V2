
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Audio"
    oIndex = "TDA7052A"
    hexID = "SZKAMPLIFIERAUDIOTDA752A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TDA7052A', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.nxp.com/docs/en/data-sheet/TDA7052A_AT.pdf', 'kicadSymbolki_keywords': 'audio amplifier', 'kicadSymbolki_description': '1W BTL mono audio amplifier with DC volume control, DIP-8/SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*7.5x9mm*P1.27mm* DIP*W7.62mm*'}])
    newPart['name'].append('TDA7052A')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

