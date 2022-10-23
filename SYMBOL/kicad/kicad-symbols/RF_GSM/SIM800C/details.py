
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_GSM"
    oIndex = "SIM800C"
    hexID = "SZKGSMSIM8C"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SIM800C', 'kicadSymbolFootprint': 'RF_GSM:SIMCom_SIM800C', 'kicadSymbolDatasheet': 'http://simcom.ee/documents/SIM800C/SIM800C_Hardware_Design_V1.05.pdf', 'kicadSymbolki_keywords': 'GSM GPRS Quad-Band SMS', 'kicadSymbolki_description': 'GSM Quad-Band Communication Module, GPRS, Audio Engine, AT Command Set, Bluetooth is Optional', 'kicadSymbolki_fp_filters': 'SIMCom*SIM800C*'}])
    newPart['name'].append('SIM800C')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

