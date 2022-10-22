
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Battery_Management"
    oIndex = "BQ24006"
    hexID = "SZKBATMANAGEMENTBQ246"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'BQ24006', 'kicadSymbolFootprint': 'Package_SO:HTSSOP-20-1EP_4.4x6.5mm_P0.65mm_EP3.4x6.5mm_Mask2.4x3.7mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/bq24006.pdf', 'kicadSymbolki_keywords': '2-Cell Li-Ion Charge', 'kicadSymbolki_description': '2-Cell Li-Ion Charge Management IC, HTSSOP-20', 'kicadSymbolki_fp_filters': 'HTSSOP*1EP*4.4x6.5mm*P0.65mm*'}])
    newPart['name'].append('BQ24006')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

