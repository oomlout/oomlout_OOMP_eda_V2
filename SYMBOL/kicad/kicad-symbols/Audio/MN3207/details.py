
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Audio"
    oIndex = "MN3207"
    hexID = "SZKAUDIOMN327"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MN3207', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.experimentalistsanonymous.com/diy/Datasheets/MN3207.pdf', 'kicadSymbolki_keywords': 'Matsushita Panasonic BBD', 'kicadSymbolki_description': '1024-STAGE LOW VOLTAGE OPERATION LOW NOISE BBD (bucket brigade device), delay time 2.56ms to 51.2ms, S/N 73dB, clock frequency range 10KHz to 200KHz', 'kicadSymbolki_fp_filters': 'DIP-8*'}])
    newPart['name'].append('MN3207')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

