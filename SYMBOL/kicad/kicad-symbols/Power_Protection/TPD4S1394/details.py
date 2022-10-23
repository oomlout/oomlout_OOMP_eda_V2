
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Protection"
    oIndex = "TPD4S1394"
    hexID = "SZKPOWERPROTECTIONTPD4S1394"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPD4S1394', 'kicadSymbolFootprint': 'Package_SON:X2SON-8_1.4x1mm_P0.35mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tpd4s1394.pdf', 'kicadSymbolki_keywords': 'firewire ESD clamp', 'kicadSymbolki_description': 'Firewire ESD Clamp With Live-Insertion Detection Circuit, X2SON-8', 'kicadSymbolki_fp_filters': 'X2SON*1.4x1mm*P0.35mm*'}])
    newPart['name'].append('TPD4S1394')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

