
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_NXP_S08"
    oIndex = "MC9S08QA2CPAE"
    hexID = "SZKMCUNXPS8MC9S8QA2CPAE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MC9S08QA4CPAE', 'kicadSymbolReference': 'IC', 'kicadSymbolValue': 'MC9S08QA2CPAE', 'kicadSymbolFootprint': 'Package_DIP:DIP-8_W7.62mm', 'kicadSymbolDatasheet': 'http://cache.nxp.com/files/microcontrollers/doc/ref_manual/MC9S08QA4RM.pdf', 'kicadSymbolki_keywords': 'NXP S08 Microcontroller', 'kicadSymbolki_description': '8-bit Small Package Microcontroller, S08 core, 2kB Flash, 160B RAM, DIP-8', 'kicadSymbolki_fp_filters': 'DIP*7.62mm*'}])
    newPart['name'].append('MCU_NXP_S08 : MC9S08QA2CPAE')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

