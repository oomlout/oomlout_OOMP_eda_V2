
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Protection"
    oIndex = "RCLAMP3328P"
    hexID = "SZKPOWERPROTECTIONRCLAMP3328P"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'RCLAMP3328P', 'kicadSymbolFootprint': 'Package_DFN_QFN:UDFN-9_1.0x3.8mm_P0.5mm', 'kicadSymbolDatasheet': 'https://media.digikey.com/pdf/Data%20Sheets/Semtech%20PDFs/RCLAMP3328P.pdf', 'kicadSymbolki_keywords': 'usb esd protection suppression transient', 'kicadSymbolki_description': 'Low Capacitance TVS Diode Array, 3.3V Standoff, 8 Channels, UDFN-9', 'kicadSymbolki_fp_filters': 'UDFN*1.0x3.8mm*P0.5mm*'}])
    newPart['name'].append('Power_Protection : RCLAMP3328P')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

