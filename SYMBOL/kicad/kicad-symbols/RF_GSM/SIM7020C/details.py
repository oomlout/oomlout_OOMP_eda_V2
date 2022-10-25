
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_GSM"
    oIndex = "SIM7020C"
    hexID = "SZKGSMSIM72C"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SIM7020E', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SIM7020C', 'kicadSymbolFootprint': 'RF_GSM:SIMCom_SIM800C', 'kicadSymbolDatasheet': 'https://simcom.ee/documents/SIM7020/SIM7020%20Hardware%20Design_V1.02.pdf', 'kicadSymbolki_keywords': 'NB-IoT Data SMS', 'kicadSymbolki_description': 'NB-IoT B1/B3/B5/B8, AT Command Set', 'kicadSymbolki_fp_filters': 'SIMCom*SIM800C*'}])
    newPart['name'].append('RF_GSM : SIM7020C')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

