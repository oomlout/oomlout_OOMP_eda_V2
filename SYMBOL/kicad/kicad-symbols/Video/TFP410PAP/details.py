
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Video"
    oIndex = "TFP410PAP"
    hexID = "SZKVIDEOTFP41PAP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TFP410PAP', 'kicadSymbolFootprint': 'Package_QFP:HTQFP-64-1EP_10x10mm_P0.5mm_EP8x8mm_Mask4.4x4.4mm_ThermalVias', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tfp410.pdf', 'kicadSymbolki_keywords': 'DVI Encoder Driver', 'kicadSymbolki_description': 'Digital Visual Interface Compliant PanelBus Digital Transmitter, HTQFP-64', 'kicadSymbolki_fp_filters': 'HTQFP*1EP*10x10mm*P0.5mm*'}])
    newPart['name'].append('TFP410PAP')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

