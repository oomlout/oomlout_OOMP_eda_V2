
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF"
    oIndex = "AQH1213A"
    hexID = "SZKRFAQH1213A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AQH0213A', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AQH1213A', 'kicadSymbolFootprint': 'Package_SO:SSO-7-8_6.4x9.78mm_P2.54mm', 'kicadSymbolDatasheet': 'https://b2b-api.panasonic.eu/file_stream/pids/fileversion/2787', 'kicadSymbolki_keywords': 'Opto-Triac Opto Triac Zero Cross Solid State Relays', 'kicadSymbolki_description': 'Zero Cross Opto-Triac, Vdrm 600V, Ift 10mA, IT 600mA, SOIC-7', 'kicadSymbolki_fp_filters': 'SSO*6.4x9.78mm*P2.54mm*'}])
    newPart['name'].append('AQH1213A')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

