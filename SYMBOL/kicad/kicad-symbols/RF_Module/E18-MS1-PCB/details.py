
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Module"
    oIndex = "E18-MS1-PCB"
    hexID = "SZKRFMOE18MS1PCB"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'E18-MS1-PCB', 'kicadSymbolFootprint': 'RF_Module:E18-MS1-PCB', 'kicadSymbolDatasheet': 'http://www.cdebyte.com/en/downpdf.aspx?id=122', 'kicadSymbolki_keywords': 'Zigbee, RF, 802.15.4', 'kicadSymbolki_description': 'Zigbee RF Module', 'kicadSymbolki_fp_filters': 'E18-MS1-PCB*'}])
    newPart['name'].append('E18-MS1-PCB')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

