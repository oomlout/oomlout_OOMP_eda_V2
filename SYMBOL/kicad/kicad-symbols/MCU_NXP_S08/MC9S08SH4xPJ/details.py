
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_NXP_S08"
    oIndex = "MC9S08SH4xPJ"
    hexID = "SZKMCUNXPS8MC9S8SH4XPJ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MC9S08SH8xPJ', 'kicadSymbolReference': 'IC', 'kicadSymbolValue': 'MC9S08SH4xPJ', 'kicadSymbolFootprint': 'Package_DIP:DIP-20_W7.62mm', 'kicadSymbolDatasheet': 'http://cache.nxp.com/files/microcontrollers/doc/data_sheet/MC9S08SH8.pdf', 'kicadSymbolki_keywords': 'NXP S08 Microcontroller', 'kicadSymbolki_description': '8-bit General Purpose Microcontroller, S08 core, 4kB Flash, 256B RAM, DIP-20', 'kicadSymbolki_fp_filters': 'DIP*7.62mm*'}])
    newPart['name'].append('MCU_NXP_S08 : MC9S08SH4xPJ')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

