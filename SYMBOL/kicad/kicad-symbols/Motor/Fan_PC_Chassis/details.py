
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Motor"
    oIndex = "Fan_PC_Chassis"
    hexID = "SZKMOTORFANPCCHASSIS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'Fan_Tacho', 'kicadSymbolReference': 'M', 'kicadSymbolValue': 'Fan_PC_Chassis', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.hardwarecanucks.com/forum/attachments/new-builds/16287d1330775095-help-chassis-power-fan-connectors-motherboard-asus_p8z68.jpg', 'kicadSymbolki_keywords': 'Fan Motor tacho', 'kicadSymbolki_description': 'PC chassis fan, tacho output, 3-pin connector', 'kicadSymbolki_fp_filters': 'FanPinHeader*P2.54mm*Vertical* PinHeader*P2.54mm*Vertical* TerminalBlock*'}])
    newPart['name'].append('Motor : Fan_PC_Chassis')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

