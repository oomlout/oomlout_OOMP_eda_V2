
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "VQFN-20-1EP_3x3mm_P0.4mm_EP1.7x1.7mm_ThermalVias"
    hexID = "FZKDFNVQFN21EP3X3P4EP17X17THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'VQFN-20-1EP_3x3mm_P0.4mm_EP1.7x1.7mm_ThermalVias', 'description': 'VQFN, 20 Pin (http://ww1.microchip.com/downloads/en/DeviceDoc/20%20Lead%20VQFN%203x3x0_9mm_1_7EP%20U2B%20C04-21496a.pdf), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'VQFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/VQFN-20-1EP_3x3mm_P0.4mm_EP1.7x1.7mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : VQFN-20-1EP_3x3mm_P0.4mm_EP1.7x1.7mm_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

