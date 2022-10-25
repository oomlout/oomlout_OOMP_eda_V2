
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "Conn_ST_STDC14"
    hexID = "SZKCNCONNSTSTDC14"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'Conn_ST_STDC14', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.st.com/content/ccc/resource/technical/document/user_manual/group1/99/49/91/b6/b2/3a/46/e5/DM00526767/files/DM00526767.pdf/jcr:content/translations/en.DM00526767.pdf', 'kicadSymbolki_keywords': 'ST STM32 Cortex Debug Connector ARM SWD JTAG', 'kicadSymbolki_description': 'ST Debug Connector, standard ARM Cortex-M SWD and JTAG interface plus UART', 'kicadSymbolki_fp_filters': 'PinHeader?2x07?P1.27mm*'}])
    newPart['name'].append('Connector : Conn_ST_STDC14')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

