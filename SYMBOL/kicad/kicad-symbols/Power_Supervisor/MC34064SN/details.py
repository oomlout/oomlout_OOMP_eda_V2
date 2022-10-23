
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Supervisor"
    oIndex = "MC34064SN"
    hexID = "SZKPOWERSUPERVISORMC3464SN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MC34064SN', 'kicadSymbolFootprint': 'Package_SO:TSOP-5_1.65x3.05mm_P0.95mm', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/MC34064-D.PDF', 'kicadSymbolki_keywords': 'Power Supervisor', 'kicadSymbolki_description': 'Undervoltage Sensing Circuit, TSOP-5', 'kicadSymbolki_fp_filters': 'TSOP*1.65x3.05mm*P0.95mm*'}])
    newPart['name'].append('MC34064SN')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

