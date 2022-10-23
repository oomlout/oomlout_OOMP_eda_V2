
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Timer"
    oIndex = "ICM7556"
    hexID = "SZKTIMERICM7556"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM556', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ICM7556', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.intersil.com/content/dam/Intersil/documents/icm7/icm7555-56.pdf', 'kicadSymbolki_keywords': 'dual timer 556', 'kicadSymbolki_description': 'Dual CMOS General Purpose Timer, DIP-14/SOIC-14', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* TSSOP*5.3x6.2mm*P0.65mm* SOIC*3.9x8.7mm*P1.27mm*'}])
    newPart['name'].append('ICM7556')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

