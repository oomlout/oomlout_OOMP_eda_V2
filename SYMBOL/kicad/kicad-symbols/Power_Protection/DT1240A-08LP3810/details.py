
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Protection"
    oIndex = "DT1240A-08LP3810"
    hexID = "SZKPOWERPROTECTIONDT124A8LP381"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'RCLAMP3328P', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'DT1240A-08LP3810', 'kicadSymbolFootprint': 'Package_DFN_QFN:UDFN-9_1.0x3.8mm_P0.5mm', 'kicadSymbolDatasheet': 'https://www.diodes.com/assets/Datasheets/DT1240A-08LP3810.pdf', 'kicadSymbolki_keywords': 'usb esd protection suppression transient', 'kicadSymbolki_description': 'Low Capacitance TVS Diode Array, 3.3V Standoff, 8 Channels, UDFN-9', 'kicadSymbolki_fp_filters': 'UDFN*1.0x3.8mm*P0.5mm*'}])
    newPart['name'].append('DT1240A-08LP3810')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

