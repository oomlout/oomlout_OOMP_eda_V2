
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Bluetooth"
    oIndex = "BM78SPPS5MC2"
    hexID = "SZKRFBLUETOOTHBM78SPPS5MC2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'BM78SPPS5MC2', 'kicadSymbolFootprint': 'RF_Module:BM78SPPS5XC2', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/60001380C.pdf', 'kicadSymbolki_keywords': 'Bluetooth BLE BT GAP SPP SDP RFCOMM L2CAP GATT ATT SMP L2CAP', 'kicadSymbolki_description': 'Bluetooth Dual-Mode, UART, Class 2', 'kicadSymbolki_fp_filters': 'BM78SPPS5XC2*'}])
    newPart['name'].append('RF_Bluetooth : BM78SPPS5MC2')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

