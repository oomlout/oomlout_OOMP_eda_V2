
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Management"
    oIndex = "PD70224"
    hexID = "SZKPOWERMANAGEMENTPD7224"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PD70224', 'kicadSymbolFootprint': 'Package_DFN_QFN:Microsemi_QFN-40-32-2EP_6x8mm_P0.5mm', 'kicadSymbolDatasheet': 'https://www.microsemi.com/document-portal/doc_download/131677-pd70224-data-sheet', 'kicadSymbolki_keywords': 'dual ideal diode bridge', 'kicadSymbolki_description': 'Ideal Dual Diode Bridge, QFN-40', 'kicadSymbolki_fp_filters': 'Microsemi*QFN*6x8mm*P0.5mm*'}])
    newPart['name'].append('PD70224')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

