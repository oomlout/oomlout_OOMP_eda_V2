
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_LGA"
    oIndex = "VLGA-4_2x2.5mm_P1.65mm"
    hexID = "FZKLGAVLGA42X25P165"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'VLGA-4_2x2.5mm_P1.65mm', 'description': 'VLGA, 4 Pin (https://ww1.microchip.com/downloads/en/DeviceDoc/DSC60XX-Ultra-Small-Ultra-Low-Power-MEMS-Oscillator-DS20005625C.pdf), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'VLGA NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_LGA.3dshapes/VLGA-4_2x2.5mm_P1.65mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_LGA : VLGA-4_2x2.5mm_P1.65mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

