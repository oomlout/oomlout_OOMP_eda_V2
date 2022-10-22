
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Battery_Management"
    oIndex = "BQ51050BRHL"
    hexID = "SZKBATMANAGEMENTBQ515BRHL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'BQ51050BRHL', 'kicadSymbolFootprint': 'Package_DFN_QFN:Texas_VQFN-RHL-20', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/bq51050b.pdf', 'kicadSymbolki_keywords': 'Qi Wireless Power Receiver Battery Charger 4.2V', 'kicadSymbolki_description': 'Qi v1.2, Wireless Power Receiver and Battery Charger, Vout 4.2V, VQFN-20', 'kicadSymbolki_fp_filters': 'Texas?VQFN?RHL*'}])
    newPart['name'].append('BQ51050BRHL')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

