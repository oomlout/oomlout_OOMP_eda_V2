
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Battery_Management"
    oIndex = "AS8506C"
    hexID = "SZKBATMANAGEMENTAS856C"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AS8506C', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-40-1EP_6x6mm_P0.5mm_EP4.6x4.6mm', 'kicadSymbolDatasheet': 'http://ams.com/eng/content/download/476603/1402377/252935', 'kicadSymbolki_keywords': 'battery balance lithium charge afe', 'kicadSymbolki_description': 'Stackable cell monitor, cell balancer, 3-7 Cells, SPI Interface', 'kicadSymbolki_fp_filters': 'QFN*6x6mm*P0.5mm*'}])
    newPart['name'].append('AS8506C')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

