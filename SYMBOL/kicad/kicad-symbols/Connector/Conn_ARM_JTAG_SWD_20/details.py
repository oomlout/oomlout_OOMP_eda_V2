
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "Conn_ARM_JTAG_SWD_20"
    hexID = "SZKCNCONNARMJTAGSWD2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'Conn_ARM_JTAG_SWD_20', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://infocenter.arm.com/help/topic/com.arm.doc.dui0499b/DUI0499B_system_design_reference.pdf', 'kicadSymbolki_keywords': 'IDC20 Male Connector ARM JTAG SWD', 'kicadSymbolki_description': 'Standard IDC20 Male Connector, ARM legacy JTAG and SWD interface', 'kicadSymbolki_fp_filters': 'IDC*Header*P2.54mm* PinHeader*2x10*P2.54mm*'}])
    newPart['name'].append('Connector : Conn_ARM_JTAG_SWD_20')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

