
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "VQFN-32-1EP_5x5mm_P0.5mm_EP3.15x3.15mm_ThermalVias"
    hexID = "FZKDFNVQFN321EP5X5P5EP315X315THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'VQFN-32-1EP_5x5mm_P0.5mm_EP3.15x3.15mm_ThermalVias', 'description': 'VQFN, 32 Pin (https://www.ti.com/lit/ds/slvs589d/slvs589d.pdf#page=33), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'VQFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/VQFN-32-1EP_5x5mm_P0.5mm_EP3.15x3.15mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : VQFN-32-1EP_5x5mm_P0.5mm_EP3.15x3.15mm_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

