
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "QFN-16-1EP_4x4mm_P0.65mm_EP2.7x2.7mm_PullBack_ThermalVias"
    hexID = "FZKDFNQFN161EP4X4P65EP27X27PULLBACKTHERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'QFN-16-1EP_4x4mm_P0.65mm_EP2.7x2.7mm_PullBack_ThermalVias', 'description': 'QFN, 16 Pin (https://ams.com/documents/20143/36005/AS5055A_DS000304_2-00.pdf#page=24), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'QFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/QFN-16-1EP_4x4mm_P0.65mm_EP2.7x2.7mm_PullBack.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : QFN-16-1EP_4x4mm_P0.65mm_EP2.7x2.7mm_PullBack_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

