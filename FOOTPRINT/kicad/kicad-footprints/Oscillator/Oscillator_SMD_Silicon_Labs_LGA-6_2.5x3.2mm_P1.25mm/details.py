
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Oscillator"
    oIndex = "Oscillator_SMD_Silicon_Labs_LGA-6_2.5x3.2mm_P1.25mm"
    hexID = "FZKOCSOCSSMSILICONLABSLGA625X32P125"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Oscillator_SMD_Silicon_Labs_LGA-6_2.5x3.2mm_P1.25mm', 'description': 'Silicon_Labs  LGA, 6 Pin (https://www.silabs.com/documents/public/data-sheets/si512-13.pdf), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'Silicon_Labs LGA NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Oscillator.3dshapes/Oscillator_SMD_Silicon_Labs_LGA-6_2.5x3.2mm_P1.25mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Oscillator : Oscillator_SMD_Silicon_Labs_LGA-6_2.5x3.2mm_P1.25mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

