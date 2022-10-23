
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Management"
    oIndex = "TPS26633RGE"
    hexID = "SZKPOWERMANAGEMENTTPS26633RGE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TPS26632RGE', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPS26633RGE', 'kicadSymbolFootprint': 'Package_DFN_QFN:Texas_RGE0024H_EP2.7x2.7mm_ThermalVias', 'kicadSymbolDatasheet': 'https://www.ti.com/lit/ds/symlink/tps2663.pdf', 'kicadSymbolki_keywords': 'efuse protection switch', 'kicadSymbolki_description': '60V, 6A Power Limiting, Surge Protection Industrial eFuse, 35V fixed Overvoltage clamp, Active Current Limiting with Pulse current support, VQFN-24', 'kicadSymbolki_fp_filters': 'Texas?RGE0024H*'}])
    newPart['name'].append('TPS26633RGE')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

