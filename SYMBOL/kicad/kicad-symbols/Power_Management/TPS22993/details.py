
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Management"
    oIndex = "TPS22993"
    hexID = "SZKPOWERMANAGEMENTTPS22993"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPS22993', 'kicadSymbolFootprint': 'Package_DFN_QFN:Texas_S-PWQFN-N20', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/gpn/tps22993', 'kicadSymbolki_keywords': 'quad channel power distribution/load switch', 'kicadSymbolki_description': 'Quad Channel Load Switch with GPIO and I2C Control, Bias voltage: 4.5V-17.2V, Input voltage: 1.0V-3.6V, Max 1.2A per channel, WQFN-20', 'kicadSymbolki_fp_filters': 'Texas*PWQFN*'}])
    newPart['name'].append('TPS22993')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

