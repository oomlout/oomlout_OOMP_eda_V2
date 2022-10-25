
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Controller"
    oIndex = "UCC3800"
    hexID = "SZKREGULATORCONTROLLERUCC38"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'UCC3800', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/ucc3800.pdf', 'kicadSymbolki_keywords': 'SMPS PWM Controller', 'kicadSymbolki_description': 'Low-Power BiCMOS Current-Mode PWM Controllers, 100% Duty Cycle, 7.2V/6.9V UVLO, DIP-8/SOIC-8/TSSOP-8', 'kicadSymbolki_fp_filters': 'TSSOP*4.4x3mm*P0.65mm* SOIC*3.9x4.9mm*P1.27mm* DIP*W7.62mm*'}])
    newPart['name'].append('Regulator_Controller : UCC3800')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

