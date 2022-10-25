
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Device"
    oIndex = "Q_Dual_NPN_PNP_E1B1C2E2B2C1"
    hexID = "SZKDEVICEQDUALNPNPNPE1B1C2E2B2C1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'Q_Dual_NPN_PNP_E1B1C2E2B2C1', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'transistor NPN PNP', 'kicadSymbolki_description': 'Dual NPN/PNP transistor, 6 pin package', 'kicadSymbolki_fp_filters': 'SC?70* SC?88* SOT?363* SOT?23*'}])
    newPart['name'].append('Device : Q_Dual_NPN_PNP_E1B1C2E2B2C1')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

