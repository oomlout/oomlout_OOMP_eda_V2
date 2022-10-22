
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Battery_Management"
    oIndex = "BQ24133RGY"
    hexID = "SZKBATMANAGEMENTBQ24133RGY"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'BQ24133RGY', 'kicadSymbolFootprint': 'Package_DFN_QFN:Texas_RGY_R-PVQFN-N24_EP2.05x3.1mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/bq24133.pdf', 'kicadSymbolki_keywords': 'Battery, Charger, Li-Ion, Li-Poly', 'kicadSymbolki_description': 'Synchronous switched mode Li-Ion and Li-Polymer battery charger, integrated MOSFETs and power path selector, Texas R-PVQFN-N24', 'kicadSymbolki_fp_filters': 'Texas*RGY*R*PVQFN*N*'}])
    newPart['name'].append('BQ24133RGY')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

