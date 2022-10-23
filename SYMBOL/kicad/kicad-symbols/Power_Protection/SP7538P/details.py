
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Protection"
    oIndex = "SP7538P"
    hexID = "SZKPOWERPROTECTIONSP7538P"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'RCLAMP3328P', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'SP7538P', 'kicadSymbolFootprint': 'Package_DFN_QFN:UDFN-9_1.0x3.8mm_P0.5mm', 'kicadSymbolDatasheet': 'https://www.littelfuse.com/~/media/electronics/datasheets/tvs_diode_arrays/littelfuse_tvs_diode_array_sp7538p_datasheet.pdf.pdf', 'kicadSymbolki_keywords': 'usb esd protection suppression transient', 'kicadSymbolki_description': 'Low Capacitance TVS Diode Array, 5.0V Standoff, 8 Channels, UDFN-9', 'kicadSymbolki_fp_filters': 'UDFN*1.0x3.8mm*P0.5mm*'}])
    newPart['name'].append('SP7538P')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

