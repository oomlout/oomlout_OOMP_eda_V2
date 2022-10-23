
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_Optical"
    oIndex = "SFP+"
    hexID = "SZKINTERFACEOPTICALSFP+"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'SFP+', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://members.snia.org/document/dl/25892', 'kicadSymbolki_keywords': 'SFP transceiver gigabit ethernet SFF-8432', 'kicadSymbolki_description': 'Connector for Small Form Factor Pluggable (SFP+) module, 10 Gbit/s, serial-to-serial data-agnostic optical transceiver', 'kicadSymbolki_fp_filters': '*SFP*'}])
    newPart['name'].append('SFP+')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

