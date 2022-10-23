
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transformer"
    oIndex = "Wuerth_749013011A"
    hexID = "SZKTRWUERTH7491311A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PT61017PEL', 'kicadSymbolReference': 'TR', 'kicadSymbolValue': 'Wuerth_749013011A', 'kicadSymbolFootprint': 'Transformer_SMD:Transformer_Ethernet_Wuerth_749013011A', 'kicadSymbolDatasheet': 'https://www.we-online.com/katalog/datasheet/749013011A.pdf', 'kicadSymbolki_keywords': 'single port ethernet transformer poe center tap', 'kicadSymbolki_description': 'Ethernet LAN 10/100 Base-Tx Transformer CT, SMD', 'kicadSymbolki_fp_filters': 'Transformer*Ethernet*Wuerth*749013011A*'}])
    newPart['name'].append('Wuerth_749013011A')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

