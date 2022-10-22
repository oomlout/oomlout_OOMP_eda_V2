
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Battery_Management"
    oIndex = "BQ24166RGE"
    hexID = "SZKBATMANAGEMENTBQ24166RGE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'BQ24166RGE', 'kicadSymbolFootprint': 'Package_DFN_QFN:Texas_RGE0024H_EP2.7x2.7mm', 'kicadSymbolDatasheet': 'https://www.ti.com/lit/ds/symlink/bq24166.pdf', 'kicadSymbolki_keywords': 'Battery, Charger, Li-Ion, Li-Poly', 'kicadSymbolki_description': 'High efficiency switched mode Li-Ion and Li-Polymer battery charger, integrated MOSFETs, power path selector and standard temperature sensing, Texas R-RGE0024H', 'kicadSymbolki_fp_filters': 'Texas*RGE0024H*'}])
    newPart['name'].append('BQ24166RGE')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

