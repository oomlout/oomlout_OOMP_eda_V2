
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Bluetooth"
    oIndex = "SPBTLE-RF0"
    hexID = "SZKRFBLUETOOTHSPBTLERF"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SPBTLE-RF', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SPBTLE-RF0', 'kicadSymbolFootprint': 'RF_Module:ST_SPBTLE', 'kicadSymbolDatasheet': 'http://www.st.com/resource/en/datasheet/spbtle-rf0.pdf', 'kicadSymbolki_keywords': 'BLE bluetooth module low-power', 'kicadSymbolki_description': 'Very Low Power network processor module for BLE v4.1', 'kicadSymbolki_fp_filters': 'ST*SPBTLE*'}])
    newPart['name'].append('SPBTLE-RF0')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

