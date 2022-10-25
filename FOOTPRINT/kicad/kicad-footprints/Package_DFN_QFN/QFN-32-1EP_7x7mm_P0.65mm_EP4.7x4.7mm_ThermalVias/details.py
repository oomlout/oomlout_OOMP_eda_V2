
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "QFN-32-1EP_7x7mm_P0.65mm_EP4.7x4.7mm_ThermalVias"
    hexID = "FZKDFNQFN321EP7X7P65EP47X47THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'QFN-32-1EP_7x7mm_P0.65mm_EP4.7x4.7mm_ThermalVias', 'description': 'QFN, 32 Pin (https://www.nxp.com/docs/en/data-sheet/LPC111X.pdf#page=108), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'QFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/QFN-32-1EP_7x7mm_P0.65mm_EP4.7x4.7mm.wrl', 'pins': {'type': 'smd', 'shape': 'custom'}})
    newPart['name'].append('Package_DFN_QFN : QFN-32-1EP_7x7mm_P0.65mm_EP4.7x4.7mm_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

