
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Relay_SolidState"
    oIndex = "AQH2213"
    hexID = "SZKRELAYSOLIDSTATEAQH2213"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AQH0213', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AQH2213', 'kicadSymbolFootprint': 'Package_DIP:DIP-8-N7_W7.62mm', 'kicadSymbolDatasheet': 'https://b2b-api.panasonic.eu/file_stream/pids/fileversion/2787', 'kicadSymbolki_keywords': 'Opto-Triac Opto Triac Zero Cross Solid State Relays', 'kicadSymbolki_description': 'Zero Cross Opto-Triac, Vdrm 600V, Ift 10mA, IT 900mA, DIP-7', 'kicadSymbolki_fp_filters': 'DIP*N7*W7.62mm*'}])
    newPart['name'].append('AQH2213')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

