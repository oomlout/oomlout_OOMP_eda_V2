
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "TPS75005RGW"
    hexID = "SZKREGULATORLINEARTPS755RGW"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPS75005RGW', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-20-1EP_5x5mm_P0.65mm_EP3.35x3.35mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tps75005.pdf', 'kicadSymbolki_keywords': 'Dual LDO Regulator Dual Integrated Power SVS Supervisor', 'kicadSymbolki_description': 'Integrated MCU Power Solution, Dual Low Drop-Out Regulator 500mA with Supervisor, VQFN20', 'kicadSymbolki_fp_filters': 'QFN*5x5mm*P0.65mm*'}])
    newPart['name'].append('TPS75005RGW')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

