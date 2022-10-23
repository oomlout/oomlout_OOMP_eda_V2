
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_Expansion"
    oIndex = "AS1115-BQFT"
    hexID = "SZKINTERFACEEXPANSIONAS1115BQFT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AS1115-BQFT', 'kicadSymbolFootprint': 'Package_DFN_QFN:TQFN-24-1EP_4x4mm_P0.5mm_EP2.8x2.8mm_PullBack_ThermalVias', 'kicadSymbolDatasheet': 'https://ams.com/documents/20143/36005/AS1115_DS000206_1-00.pdf/3d3e6d35-b184-1329-adf9-2d769eb2404f', 'kicadSymbolki_keywords': 'led driver i2c', 'kicadSymbolki_description': '64 LEDs, I2C Interfaced LED Driver with Keyscan, TQFN-24', 'kicadSymbolki_fp_filters': 'TQFN*1EP*4x4mm*P0.5mm*PullBack*'}])
    newPart['name'].append('AS1115-BQFT')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

