
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Battery_Management"
    oIndex = "BQ25570"
    hexID = "SZKBATMANAGEMENTBQ2557"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'BQ25570', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-20-1EP_3.5x3.5mm_P0.5mm_EP2x2mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/bq25570.pdf', 'kicadSymbolki_keywords': 'harvester solar TEG charger li-on buck', 'kicadSymbolki_description': 'Nano Power Boost Charger and Buck Converter for Energy Harvester Powered Applications, QFN-20', 'kicadSymbolki_fp_filters': 'QFN*1EP*3.5x3.5mm*P0.5mm*'}])
    newPart['name'].append('BQ25570')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

