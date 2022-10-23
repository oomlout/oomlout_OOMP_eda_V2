
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_WiFi"
    oIndex = "HF-A11-SMT"
    hexID = "SZKRFHFA11S"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'HF-A11-SMT', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.hi-flying.com/index.php?route=tool/upload/download&code=190ec6c62d497905ed783d140f8e5af7a753b8ab', 'kicadSymbolki_keywords': 'WiFi IEEE802.11 b/g/n', 'kicadSymbolki_description': 'WiFi IEEE802.11b/g/n with Ethernet Module, UART, GPIO'}])
    newPart['name'].append('HF-A11-SMT')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

