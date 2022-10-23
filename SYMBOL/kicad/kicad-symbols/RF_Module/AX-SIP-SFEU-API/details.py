
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Module"
    oIndex = "AX-SIP-SFEU-API"
    hexID = "SZKRFMOAXSIPSFEUAPI"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AX-SIP-SFEU-API', 'kicadSymbolFootprint': 'Package_DFN_QFN:OnSemi_SIP-38-6EP-9x7mm_P0.65mm_EP1.2x1.2mm', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/AX-SIP-SFEU-D.PDF', 'kicadSymbolki_keywords': 'Sigfox SIP 868Mhz', 'kicadSymbolki_description': 'Ultra low power, Sigfox or custom, programmable system in package, 868Mhz', 'kicadSymbolki_fp_filters': 'OnSemi*SIP*6EP*9x7mm*P0.65mm*'}])
    newPart['name'].append('AX-SIP-SFEU-API')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

