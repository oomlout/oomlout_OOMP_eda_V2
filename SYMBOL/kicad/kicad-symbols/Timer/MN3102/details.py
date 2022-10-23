
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Timer"
    oIndex = "MN3102"
    hexID = "SZKTIMERMN312"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MN3101', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MN3102', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.experimentalistsanonymous.com/diy/Datasheets/MN3102.pdf', 'kicadSymbolki_keywords': 'Matsushita Panasonic BBD CMOS', 'kicadSymbolki_description': 'Clock Generator Driver/Driver for MN3000 Series BBD (bucket brigade device), 4V to 10V, DIP-8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('MN3102')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

