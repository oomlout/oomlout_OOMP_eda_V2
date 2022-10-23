
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF"
    oIndex = "34.81-8240"
    hexID = "SZKRF3481824"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': '34.81-8240', 'kicadSymbolFootprint': 'OptoDevice:Finder_34.81', 'kicadSymbolDatasheet': 'https://gfinder.findernet.com/public/attachments/34/EN/S34USAEN.pdf', 'kicadSymbolki_keywords': 'Photo-Triac Opto Triac', 'kicadSymbolki_description': 'Ultra-slim - Solid State Relay, 2A, 240V AC output, Zero crossing switching', 'kicadSymbolki_fp_filters': 'Finder*34.81*'}])
    newPart['name'].append('34.81-8240')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

