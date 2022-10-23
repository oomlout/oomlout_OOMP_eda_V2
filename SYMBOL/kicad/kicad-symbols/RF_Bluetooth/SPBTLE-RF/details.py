
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Bluetooth"
    oIndex = "SPBTLE-RF"
    hexID = "SZKRFBLUETOOTHSPBTLERF"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SPBTLE-RF', 'kicadSymbolFootprint': 'RF_Module:ST_SPBTLE', 'kicadSymbolDatasheet': 'http://www.st.com/resource/en/datasheet/spbtle-rf.pdf', 'kicadSymbolki_keywords': 'BLE bluetooth module low-power', 'kicadSymbolki_description': 'Very Low Power network processor module for BLE v4.1, Hub capabilities', 'kicadSymbolki_fp_filters': 'ST*SPBTLE*'}])
    newPart['name'].append('SPBTLE-RF')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

