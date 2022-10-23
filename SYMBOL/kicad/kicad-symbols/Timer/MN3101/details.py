
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Timer"
    oIndex = "MN3101"
    hexID = "SZKTIMERMN311"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MN3101', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.experimentalistsanonymous.com/diy/Datasheets/MN3101.pdf', 'kicadSymbolki_keywords': 'Matsushita Panasonic BBD CMOS', 'kicadSymbolki_description': 'Clock Generator Driver/Driver for MN3000 Series BBD (bucket brigade device), -8V to -16V, DIP-8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('MN3101')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

