
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Management"
    oIndex = "TPS26631PWP"
    hexID = "SZKPOWERMANAGEMENTTPS26631PWP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPS26631PWP', 'kicadSymbolFootprint': 'Package_SO:HTSSOP-20-1EP_4.4x6.5mm_P0.65mm_EP3.4x6.5mm_Mask2.96x2.96mm_ThermalVias', 'kicadSymbolDatasheet': 'https://www.ti.com/lit/ds/symlink/tps2663.pdf', 'kicadSymbolki_keywords': 'efuse protection switch', 'kicadSymbolki_description': '60V, 6A Power Limiting, Surge Protection Industrial eFuse, Adjustable Overvoltage cut-off, Active Current Limiting with Pulse current support, HTTSOP-20', 'kicadSymbolki_fp_filters': 'HTSSOP*1EP*4.4x6.5mm*P0.65mm*'}])
    newPart['name'].append('TPS26631PWP')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

