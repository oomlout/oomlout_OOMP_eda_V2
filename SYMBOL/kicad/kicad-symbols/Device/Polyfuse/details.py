
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Device"
    oIndex = "Polyfuse"
    hexID = "SZKDEVICEPOLYFU"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'F', 'kicadSymbolValue': 'Polyfuse', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'resettable fuse PTC PPTC polyfuse polyswitch', 'kicadSymbolki_description': 'Resettable fuse, polymeric positive temperature coefficient', 'kicadSymbolki_fp_filters': '*polyfuse* *PTC*'}])
    newPart['name'].append('Device : Polyfuse')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

