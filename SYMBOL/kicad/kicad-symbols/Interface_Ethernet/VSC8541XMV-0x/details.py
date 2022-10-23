
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_Ethernet"
    oIndex = "VSC8541XMV-0x"
    hexID = "SZKINTERFACEETHERNETVSC8541XMVX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'VSC8541XMV-0x', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-68-1EP_8x8mm_P0.4mm_EP5.2x5.2mm', 'kicadSymbolDatasheet': 'https://ethernet.microsemi.com/products/download.php?fid=7978&number=vsc8541', 'kicadSymbolki_keywords': 'Gigabit Ethernet PHY GMII RGMII MII RMII', 'kicadSymbolki_description': 'Single Port Gigabit Ethernet, GMII/RGMII/MII/RMII Interfaces, QFN-68', 'kicadSymbolki_fp_filters': 'QFN?68*1EP*8x8mm*P0.4mm*'}])
    newPart['name'].append('VSC8541XMV-0x')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

