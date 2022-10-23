
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Triac_Thyristor"
    oIndex = "BTA16-800BW"
    hexID = "SZKTRIACTHYRISTORBTA168BW"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TIC226', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'BTA16-800BW', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-220-3_Vertical', 'kicadSymbolDatasheet': 'https://www.st.com/resource/en/datasheet/bta16.pdf', 'kicadSymbolki_keywords': 'Triac', 'kicadSymbolki_description': '16A RMS, 800V Off-State Voltage, 50mA Sensitivity, Snubberless, Insulated, Triac, TO-220', 'kicadSymbolki_fp_filters': 'TO?220*'}])
    newPart['name'].append('BTA16-800BW')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

