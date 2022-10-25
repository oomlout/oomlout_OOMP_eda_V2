
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Pressure"
    oIndex = "MS5525DSO"
    hexID = "SZKSENPRESSUREMS5525DSO"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MS5525DSO', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.te.com/commerce/DocumentDelivery/DDEController?Action=srchrtrv&DocNm=MS5525DSO&DocType=DS&DocLang=English', 'kicadSymbolki_keywords': '24bit low-power I2C SPI', 'kicadSymbolki_description': 'Integrated Digital Pressure Sensor', 'kicadSymbolki_fp_filters': 'TE?MS5525DSO*DB* TE?MS5525DSO*SB* TE?MS5525DSO*ST* TE?MS5525DSO*DH* TE?MS5525DSO*FT* TE?MS5525DSO*FB*'}])
    newPart['name'].append('Sensor_Pressure : MS5525DSO')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

