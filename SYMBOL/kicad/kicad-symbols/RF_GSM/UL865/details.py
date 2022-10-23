
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_GSM"
    oIndex = "UL865"
    hexID = "SZKGSMUL865"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'UL865', 'kicadSymbolFootprint': 'RF_GSM:Telit_xL865', 'kicadSymbolDatasheet': 'http://www.telit.com/fileadmin/user_upload/products/Downloads/3G/Telit_UL865_Hardware_User_Guide_r8.pdf', 'kicadSymbolki_keywords': 'gsm 3g gprs umts hspa', 'kicadSymbolki_description': 'Telit 3G Module (GSM/GPRS/UMTS/HSPA), 3.8V, Digital voice and SMS, I2S, USB 2.0, UART, SPI. Manufacturer package', 'kicadSymbolki_fp_filters': '*Telit*xL865*'}])
    newPart['name'].append('UL865')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

