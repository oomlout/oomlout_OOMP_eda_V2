
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transformer"
    oIndex = "TG110-S050N2xx"
    hexID = "SZKTRTG11S5N2XX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TG110-E050N5xx', 'kicadSymbolReference': 'TR', 'kicadSymbolValue': 'TG110-S050N2xx', 'kicadSymbolFootprint': 'Transformer_SMD:Transformer_Ethernet_Halo_N2_SO-16_7.11x12.7mm', 'kicadSymbolDatasheet': 'https://www.haloelectronics.com/pdf/discrete-ultra-100baset.pdf', 'kicadSymbolki_keywords': 'single port ethernet transformer', 'kicadSymbolki_description': 'Ethernet LAN 10/100 Base-Tx Transformer', 'kicadSymbolki_fp_filters': 'Transformer*Ethernet*Halo*N2*'}])
    newPart['name'].append('TG110-S050N2xx')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

