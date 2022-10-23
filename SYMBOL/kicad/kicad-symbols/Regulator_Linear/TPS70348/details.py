
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "TPS70348"
    hexID = "SZKREGULATORLINEARTPS7348"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TPS70302', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPS70348', 'kicadSymbolFootprint': 'Package_SO:HTSSOP-24-1EP_4.4x7.8mm_P0.65mm_EP3.4x7.8mm_Mask2.4x4.68mm_ThermalVias', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tps703.pdf', 'kicadSymbolki_keywords': 'dual ldo regulator', 'kicadSymbolki_description': 'Dual-Output, Low Dropout Voltage Regulators With Integrated SVS For Split Voltage Systems, Sequenced Outputs, 3.3V 1A/1.5V 2A, HTSSOP-24', 'kicadSymbolki_fp_filters': 'HTSSOP*4.4x7.8mm*P0.65mm*'}])
    newPart['name'].append('TPS70348')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

