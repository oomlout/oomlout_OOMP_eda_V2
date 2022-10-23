
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transformer"
    oIndex = "TG111-MSC13LF"
    hexID = "SZKTRTG111MSC13LF"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'TR', 'kicadSymbolValue': 'TG111-MSC13LF', 'kicadSymbolFootprint': 'Transformer_SMD:Transformer_Ethernet_HALO_TG111-MSC13', 'kicadSymbolDatasheet': 'https://www.haloelectronics.com/pdf/discrete-genesus.pdf', 'kicadSymbolki_keywords': 'Single Port Gigabit Ethernet Transformer', 'kicadSymbolki_description': 'Single Port Gigabit Ethernet Transformers', 'kicadSymbolki_fp_filters': 'Transformer*Ethernet*HALO*TG111*'}])
    newPart['name'].append('TG111-MSC13LF')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

