
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Controller"
    oIndex = "UCC3813-0"
    hexID = "SZKREGULATORCONTROLLERUCC3813"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'UCC3800', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'UCC3813-0', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/ucc3813-1.pdf', 'kicadSymbolki_keywords': 'SMPS PWM Controller', 'kicadSymbolki_description': 'Low-Power Economy BiCMOS Current-Mode PWM, 100% Duty Cycle, 7.2V/6.9V UVLO, DIP-8/SOIC-8/TSSOP-8', 'kicadSymbolki_fp_filters': 'TSSOP*4.4x3mm*P0.65mm* SOIC*3.9x4.9mm*P1.27mm* DIP*W7.62mm*'}])
    newPart['name'].append('Regulator_Controller : UCC3813-0')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

