
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Protection"
    oIndex = "ESDLC5V0PB8"
    hexID = "SZKPOWERPROTECTIONESDLC5VPB8"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'RCLAMP3328P', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'ESDLC5V0PB8', 'kicadSymbolFootprint': 'Package_DFN_QFN:UDFN-9_1.0x3.8mm_P0.5mm', 'kicadSymbolDatasheet': 'https://www.mccsemi.com/pdf/Products/ESDLC5V0PB8(DFN3810-9)-A.pdf', 'kicadSymbolki_keywords': 'usb esd protection suppression transient', 'kicadSymbolki_description': 'TVS Diode Array, 5.0V Standoff, 8 Channels, UDFN-9', 'kicadSymbolki_fp_filters': 'UDFN*1.0x3.8mm*P0.5mm*'}])
    newPart['name'].append('Power_Protection : ESDLC5V0PB8')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

