
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Protection"
    oIndex = "WE-TVS-824014881"
    hexID = "SZKPOWERPROTECTIONWETVS82414881"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'RCLAMP3328P', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'WE-TVS-824014881', 'kicadSymbolFootprint': 'Package_DFN_QFN:UDFN-9_1.0x3.8mm_P0.5mm', 'kicadSymbolDatasheet': 'https://katalog.we-online.de/pbs/datasheet/824014881.pdf', 'kicadSymbolki_keywords': 'usb esd protection suppression transient', 'kicadSymbolki_description': 'TVS Diode Array, 1.2V Standoff, 8 Channels, UDFN-9', 'kicadSymbolki_fp_filters': 'UDFN*1.0x3.8mm*P0.5mm*'}])
    newPart['name'].append('Power_Protection : WE-TVS-824014881')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

