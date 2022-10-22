
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "Conn_ARM_JTAG_SWD_10"
    hexID = "SZKCNCONNARMJTAGSWD1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'Conn_ARM_JTAG_SWD_10', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://infocenter.arm.com/help/topic/com.arm.doc.ddi0314h/DDI0314H_coresight_components_trm.pdf', 'kicadSymbolki_keywords': 'Cortex Debug Connector ARM SWD JTAG', 'kicadSymbolki_description': 'Cortex Debug Connector, standard ARM Cortex-M SWD and JTAG interface', 'kicadSymbolki_fp_filters': 'PinHeader?2x05?P1.27mm*'}])
    newPart['name'].append('Conn_ARM_JTAG_SWD_10')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

