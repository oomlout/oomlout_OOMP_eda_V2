
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Module"
    oIndex = "TR-72DA"
    hexID = "SZKRFMOTR72DA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TR-52DA', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TR-72DA', 'kicadSymbolFootprint': 'RF_Module:IQRF_TRx2DA_KON-SIM-01', 'kicadSymbolDatasheet': 'https://iqrf.org/weben/downloads.php?id=337', 'kicadSymbolki_keywords': 'IQRF transceiver, PCB antenna, GMSK modulation', 'kicadSymbolki_description': 'IQRF transceiver with PCB antenna, GMSK modulation', 'kicadSymbolki_fp_filters': 'IQRF?TRx2DA?KON?SIM?01*'}])
    newPart['name'].append('RF_Module : TR-72DA')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

