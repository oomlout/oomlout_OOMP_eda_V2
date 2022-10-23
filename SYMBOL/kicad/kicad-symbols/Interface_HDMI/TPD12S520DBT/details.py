
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_HDMI"
    oIndex = "TPD12S520DBT"
    hexID = "SZKINTERFACEHDMITPD12S52DBT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPD12S520DBT', 'kicadSymbolFootprint': 'Package_SO:TSSOP-38_4.4x9.7mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tpd12s520.pdf', 'kicadSymbolki_keywords': 'hdmi', 'kicadSymbolki_description': 'HDMI Receiver Port Protection and Interface Device, TSSOP-38', 'kicadSymbolki_fp_filters': 'TSSOP*4.4x9.7mm*P0.5mm*'}])
    newPart['name'].append('TPD12S520DBT')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

