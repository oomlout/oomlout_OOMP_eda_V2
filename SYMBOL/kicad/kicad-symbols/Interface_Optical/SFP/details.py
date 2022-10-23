
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_Optical"
    oIndex = "SFP"
    hexID = "SZKINTERFACEOPTICALSFP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'SFP', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.10gtek.com/templates/wzten/pdf/INF-8074.pdf', 'kicadSymbolki_keywords': 'SFP transceiver gigabit ethernet INF-8074i', 'kicadSymbolki_description': 'Connector for Small Form Factor Pluggable (SFP) module, 1 Gbit/s, serial-to-serial data-agnostic optical transceiver', 'kicadSymbolki_fp_filters': '*SFP*'}])
    newPart['name'].append('SFP')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

