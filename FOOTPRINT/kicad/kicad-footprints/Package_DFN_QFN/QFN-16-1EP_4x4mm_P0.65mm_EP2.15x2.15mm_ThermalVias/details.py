
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "QFN-16-1EP_4x4mm_P0.65mm_EP2.15x2.15mm_ThermalVias"
    hexID = "FZKDFNQFN161EP4X4P65EP215X215THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'QFN-16-1EP_4x4mm_P0.65mm_EP2.15x2.15mm_ThermalVias', 'description': 'QFN, 16 Pin (https://www.analog.com/media/en/technical-documentation/data-sheets/4001f.pdf), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'QFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/QFN-16-1EP_4x4mm_P0.65mm_EP2.15x2.15mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : QFN-16-1EP_4x4mm_P0.65mm_EP2.15x2.15mm_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

