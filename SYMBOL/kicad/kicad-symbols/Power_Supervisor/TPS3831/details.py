
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Supervisor"
    oIndex = "TPS3831"
    hexID = "SZKPOWERSUPERVISORTPS3831"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPS3831', 'kicadSymbolFootprint': 'Package_SON:Texas_X2SON-4_1x1mm_P0.65mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/sbvs193d/sbvs193d.pdf', 'kicadSymbolki_keywords': 'supply voltage supervisor', 'kicadSymbolki_description': '150-nA, Ultralow Power, Supply Voltage Monitor, X2SON-4', 'kicadSymbolki_fp_filters': 'Texas*X2SON*1x1mm*P0.65mm*'}])
    newPart['name'].append('TPS3831')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

