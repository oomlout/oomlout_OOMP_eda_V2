
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_Power_Module"
    oIndex = "MG1275W-XN2MM"
    hexID = "SZKTRANSISTORPOWERMOMG1275WXN2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MG1275W-XN2MM', 'kicadSymbolFootprint': 'Transistor_Power_Module:Littelfuse_Package_W_XN2MM', 'kicadSymbolDatasheet': 'https://www.littelfuse.com/~/media/electronics/datasheets/power_semiconductors/littelfuse_power_semiconductor_igbt_module_mg1275w_xn2mm_datasheet.pdf.pdf', 'kicadSymbolki_keywords': 'IGBT Power Module Trench Field Stop Technology', 'kicadSymbolki_description': '75A, 1200V, 368W x 6 , 3-phase, Freewheeling Diode, 5k NTC, Package-W (XN2MM)', 'kicadSymbolki_fp_filters': 'Littelfuse*Package*W*XN2MM*'}])
    newPart['name'].append('MG1275W-XN2MM')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

