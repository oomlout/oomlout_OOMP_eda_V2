
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "TLV76718DRVx"
    hexID = "SZKREGULATORLINEARTLV76718DRVX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TLV76750DRVx', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TLV76718DRVx', 'kicadSymbolFootprint': 'Package_SON:WSON-6-1EP_2x2mm_P0.65mm_EP1x1.6mm_ThermalVias', 'kicadSymbolDatasheet': 'www.ti.com/lit/gpn/TLV767', 'kicadSymbolki_keywords': '1A Precision Linear Voltage Regulator', 'kicadSymbolki_description': '1A Precision Linear Voltage Regulator, with enable pin, Fixed Output 1.8V, WSON6', 'kicadSymbolki_fp_filters': 'WSON*1EP*2x2mm*P0.65*'}])
    newPart['name'].append('Regulator_Linear : TLV76718DRVx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

