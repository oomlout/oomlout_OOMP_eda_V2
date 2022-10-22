
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Battery_Management"
    oIndex = "BQ2501x"
    hexID = "SZKBATMANAGEMENTBQ251X"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'BQ2501x', 'kicadSymbolFootprint': 'Package_DFN_QFN:Texas_VQFN-RHL-20_ThermalVias', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/bq25010.pdf', 'kicadSymbolki_keywords': 'Li-ion buck', 'kicadSymbolki_description': '500mA Li-Ion Charger w/Integrated 150mA Synchronous Buck Converter, QFN-14', 'kicadSymbolki_fp_filters': 'Texas?VQFN?RHL*'}])
    newPart['name'].append('BQ2501x')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

