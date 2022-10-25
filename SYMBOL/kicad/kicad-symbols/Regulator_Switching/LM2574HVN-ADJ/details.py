
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LM2574HVN-ADJ"
    hexID = "SZKREGULATORSWITCHINGLM2574HVNADJ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM2574HVN-12', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM2574HVN-ADJ', 'kicadSymbolFootprint': 'Package_DIP:DIP-8_W7.62mm', 'kicadSymbolDatasheet': 'http://www.national.com/ds/LM/LM2574.pdf', 'kicadSymbolki_keywords': 'Step-Down Voltage Regulator Adjustable 500mA HV', 'kicadSymbolki_description': 'Adjustable Output Voltage, 0.5A SIMPLE SWITCHER® Step-Down Voltage Regulator, High Voltage Input, DIP-8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('Regulator_Switching : LM2574HVN-ADJ')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

