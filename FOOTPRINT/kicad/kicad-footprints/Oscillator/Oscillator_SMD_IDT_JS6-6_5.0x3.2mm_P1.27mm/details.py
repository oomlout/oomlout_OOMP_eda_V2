
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Oscillator"
    oIndex = "Oscillator_SMD_IDT_JS6-6_5.0x3.2mm_P1.27mm"
    hexID = "FZKOCSOCSSMIDTJS665X32P127"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Oscillator_SMD_IDT_JS6-6_5.0x3.2mm_P1.27mm', 'description': 'SMD Crystal Oscillator IDT https://www.idt.com/document/dst/xu-family-datasheet#page=15, 5.0x3.2mm', 'tags': 'SMD SMT crystal oscillator', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Oscillator.3dshapes/Oscillator_SMD_IDT_JS6-6_5.0x3.2mm_P1.27mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Oscillator : Oscillator_SMD_IDT_JS6-6_5.0x3.2mm_P1.27mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

