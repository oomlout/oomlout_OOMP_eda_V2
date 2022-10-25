
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Timer_RTC"
    oIndex = "RV-1805-C3"
    hexID = "SZKTIMERRTCRV185C3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'RV-1805-C3', 'kicadSymbolFootprint': 'Package_SON:RTC_SMD_MicroCrystal_C3_2.5x3.7mm', 'kicadSymbolDatasheet': 'https://www.microcrystal.com/fileadmin/Media/Products/RTC/Datasheet/RV-1805-C3.pdf', 'kicadSymbolki_keywords': 'Low Power RTC I2C', 'kicadSymbolki_description': 'Realtime Clock/Calendar I2C Interface, Extreme Low Power, MicroCrystal C3', 'kicadSymbolki_fp_filters': 'RTC*SMD*MicroCrystal*C3*2.5x3.7mm*'}])
    newPart['name'].append('Timer_RTC : RV-1805-C3')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

