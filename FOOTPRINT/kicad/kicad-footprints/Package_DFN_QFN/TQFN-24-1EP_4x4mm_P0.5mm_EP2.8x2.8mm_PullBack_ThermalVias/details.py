
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "TQFN-24-1EP_4x4mm_P0.5mm_EP2.8x2.8mm_PullBack_ThermalVias"
    hexID = "FZKDFNTQFN241EP4X4P5EP28X28PULLBACKTHERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TQFN-24-1EP_4x4mm_P0.5mm_EP2.8x2.8mm_PullBack_ThermalVias', 'description': 'TQFN, 24 Pin (https://ams.com/documents/20143/36005/AS1115_DS000206_1-00.pdf), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'TQFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/TQFN-24-1EP_4x4mm_P0.5mm_EP2.8x2.8mm_PullBack.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : TQFN-24-1EP_4x4mm_P0.5mm_EP2.8x2.8mm_PullBack_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

