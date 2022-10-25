
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Module"
    oIndex = "TR-52DA"
    hexID = "SZKRFMOTR52DA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TR-52DA', 'kicadSymbolFootprint': 'RF_Module:IQRF_TRx2DA_KON-SIM-01', 'kicadSymbolDatasheet': 'https://iqrf.org/weben/downloads.php?id=213', 'kicadSymbolki_keywords': 'IQRF common transceiver, PCB antenna, FSK modulation', 'kicadSymbolki_description': 'IQRF common transceiver with PCB antenna, FSK modulation', 'kicadSymbolki_fp_filters': 'IQRF?TRx2DA?KON?SIM?01*'}])
    newPart['name'].append('RF_Module : TR-52DA')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

