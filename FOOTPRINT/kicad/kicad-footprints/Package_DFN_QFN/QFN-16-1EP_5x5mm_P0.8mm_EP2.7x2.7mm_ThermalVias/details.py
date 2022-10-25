
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "QFN-16-1EP_5x5mm_P0.8mm_EP2.7x2.7mm_ThermalVias"
    hexID = "FZKDFNQFN161EP5X5P8EP27X27THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'QFN-16-1EP_5x5mm_P0.8mm_EP2.7x2.7mm_ThermalVias', 'description': 'QFN, 16 Pin (http://www.intersil.com/content/dam/Intersil/documents/l16_/l16.5x5.pdf), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'QFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/QFN-16-1EP_5x5mm_P0.8mm_EP2.7x2.7mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : QFN-16-1EP_5x5mm_P0.8mm_EP2.7x2.7mm_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

