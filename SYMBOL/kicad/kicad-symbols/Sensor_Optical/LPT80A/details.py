
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Optical"
    oIndex = "LPT80A"
    hexID = "SZKSENOPTICALLPT8A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'LPT80A', 'kicadSymbolFootprint': 'OptoDevice:Osram_LPT80A', 'kicadSymbolDatasheet': 'http://www.osram-os.com/Graphics/XPic4/00209607_0.pdf/LPT%2080A.pdf', 'kicadSymbolki_keywords': 'NPN phototransistor', 'kicadSymbolki_description': 'NPN phototransistor', 'kicadSymbolki_fp_filters': 'Osram*LPT80A*'}])
    newPart['name'].append('LPT80A')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

