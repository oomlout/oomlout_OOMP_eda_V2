
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Triac_Thyristor"
    oIndex = "BTB16-600C"
    hexID = "SZKTRIACTHYRISTORBTB166C"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TIC226', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'BTB16-600C', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-220-3_Vertical', 'kicadSymbolDatasheet': 'https://www.st.com/resource/en/datasheet/bta16.pdf', 'kicadSymbolki_keywords': 'Triac', 'kicadSymbolki_description': '16A RMS, 600V Off-State Voltage, 35mA Sensitivity, Non-Insulated, Triac, TO-220', 'kicadSymbolki_fp_filters': 'TO?220*'}])
    newPart['name'].append('Triac_Thyristor : BTB16-600C')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

