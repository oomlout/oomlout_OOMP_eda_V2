
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Module"
    oIndex = "MDBT50Q-1MV2"
    hexID = "SZKRFMOMDBT5Q1MV2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MDBT50Q-1MV2', 'kicadSymbolFootprint': 'RF_Module:Raytac_MDBT50Q', 'kicadSymbolDatasheet': 'https://www.raytac.com/download/index.php?index_id=43', 'kicadSymbolki_keywords': 'BLE ANT ZigBee Thread 802.15.4 nRF52840 nordic MDBT50Q', 'kicadSymbolki_description': 'Multiprotocol BLE/ANT/2.4 GHz/802.15.4 Cortex-M4F SoC, nRF52840 module', 'kicadSymbolki_fp_filters': 'Raytac?MDBT50Q*'}])
    newPart['name'].append('RF_Module : MDBT50Q-1MV2')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

