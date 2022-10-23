
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transformer"
    oIndex = "PT61017PEL"
    hexID = "SZKTRPT6117PEL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'TR', 'kicadSymbolValue': 'PT61017PEL', 'kicadSymbolFootprint': 'Transformer_SMD:Transformer_Ethernet_Bourns_PT61017PEL', 'kicadSymbolDatasheet': 'https://www.bourns.com/docs/Product-Datasheets/PT61017PEL.pdf', 'kicadSymbolki_keywords': 'single port ethernet transformer poe center-tap', 'kicadSymbolki_description': 'Ethernet LAN 10/100 Base-Tx Transformer with Center Taps', 'kicadSymbolki_fp_filters': 'Transformer*Ethernet*Bourns*PT61017PEL*'}])
    newPart['name'].append('PT61017PEL')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

