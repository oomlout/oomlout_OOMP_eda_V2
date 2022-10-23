
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "TLV76728DRVx"
    hexID = "SZKREGULATORLINEARTLV76728DRVX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TLV76750DRVx', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TLV76728DRVx', 'kicadSymbolFootprint': 'Package_SON:WSON-6-1EP_2x2mm_P0.65mm_EP1x1.6mm_ThermalVias', 'kicadSymbolDatasheet': 'www.ti.com/lit/gpn/TLV767', 'kicadSymbolki_keywords': '1A Precision Linear Voltage Regulator', 'kicadSymbolki_description': '1A Precision Linear Voltage Regulator, with enable pin, Fixed Output 2.8V, WSON6', 'kicadSymbolki_fp_filters': 'WSON*1EP*2x2mm*P0.65*'}])
    newPart['name'].append('TLV76728DRVx')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

