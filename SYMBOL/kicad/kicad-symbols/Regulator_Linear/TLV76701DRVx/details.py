
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "TLV76701DRVx"
    hexID = "SZKREGULATORLINEARTLV7671DRVX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TLV76701DRVx', 'kicadSymbolFootprint': 'Package_SON:WSON-6-1EP_2x2mm_P0.65mm_EP1x1.6mm_ThermalVias', 'kicadSymbolDatasheet': 'www.ti.com/lit/gpn/TLV767', 'kicadSymbolki_keywords': '1A, 16V Precision Linear Voltage Regulator', 'kicadSymbolki_description': '1A, 16V Precision Linear Voltage Regulator, with enable pin, Adjustable Output 0.8-13.6V, WSON-6', 'kicadSymbolki_fp_filters': 'WSON*1EP*2x2mm*P0.65*'}])
    newPart['name'].append('TLV76701DRVx')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

