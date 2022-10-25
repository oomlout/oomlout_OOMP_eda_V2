
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_USB"
    oIndex = "FUSB307BMPX"
    hexID = "SZKINTERFACEUFU37BMPX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'FUSB307BMPX', 'kicadSymbolFootprint': 'Package_DFN_QFN:WQFN-16-1EP_3x3mm_P0.5mm_EP1.75x1.75mm', 'kicadSymbolDatasheet': 'http://www.onsemi.com/pub/Collateral/FUSB307B-D.PDF', 'kicadSymbolki_keywords': 'USB USB-C PD Power Delivery PHY TCPC', 'kicadSymbolki_description': 'USB Type-C Port Controller with USB-PD, WQFN-16', 'kicadSymbolki_fp_filters': 'WQFN*3x3mm*P0.5mm*EP1.75x1.75mm*'}])
    newPart['name'].append('Interface_USB : FUSB307BMPX')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

