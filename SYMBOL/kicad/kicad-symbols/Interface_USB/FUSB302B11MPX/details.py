
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_USB"
    oIndex = "FUSB302B11MPX"
    hexID = "SZKINTERFACEUFU32B11MPX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'FUSB302BMPX', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'FUSB302B11MPX', 'kicadSymbolFootprint': 'Package_DFN_QFN:WQFN-14-1EP_2.5x2.5mm_P0.5mm_EP1.45x1.45mm', 'kicadSymbolDatasheet': 'http://www.onsemi.com/pub/Collateral/FUSB302B-D.PDF', 'kicadSymbolki_keywords': 'USB USB-C PD Power Delivery PHY', 'kicadSymbolki_description': 'Programmable USB Type-C Controller w/PD, I2C address 0x25, WQFN-14', 'kicadSymbolki_fp_filters': 'WQFN*2.5x2.5mm*P0.5mm*EP1.45x1.45mm*'}])
    newPart['name'].append('Interface_USB : FUSB302B11MPX')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

