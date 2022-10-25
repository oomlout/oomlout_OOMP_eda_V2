
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_Array"
    oIndex = "ULN2002"
    hexID = "SZKTRANSISTORARRAYULN22"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ULN2003', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ULN2002', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/uln2003a.pdf', 'kicadSymbolki_keywords': 'darlington transistor array', 'kicadSymbolki_description': 'High Voltage, High Current Darlington Transistor Arrays, SOIC16/SOIC16W/DIP16/TSSOP16', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* SOIC*3.9x9.9mm*P1.27mm* SSOP*4.4x5.2mm*P0.65mm* TSSOP*4.4x5mm*P0.65mm* SOIC*W*5.3x10.2mm*P1.27mm*'}])
    newPart['name'].append('Transistor_Array : ULN2002')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

