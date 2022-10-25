
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Module"
    oIndex = "MDBT50Q-P512K"
    hexID = "SZKRFMOMDBT5QP512K"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MDBT50Q-512K', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MDBT50Q-P512K', 'kicadSymbolFootprint': 'RF_Module:Raytac_MDBT50Q', 'kicadSymbolDatasheet': 'https://www.raytac.com/download/index.php?index_id=46', 'kicadSymbolki_keywords': 'MCU, ARM, BLE, ANT, 2.4GHz, 802.15.4 MDBT50Q', 'kicadSymbolki_description': 'Multiprotocol BLE/ANT/2.4 GHz/802.15.4 Cortex-M4F SoC, nRF52833 module', 'kicadSymbolki_fp_filters': 'Raytac?MDBT50Q*'}])
    newPart['name'].append('RF_Module : MDBT50Q-P512K')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

