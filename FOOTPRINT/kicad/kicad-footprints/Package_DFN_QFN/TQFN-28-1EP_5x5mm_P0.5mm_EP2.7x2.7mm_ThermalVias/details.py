
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "TQFN-28-1EP_5x5mm_P0.5mm_EP2.7x2.7mm_ThermalVias"
    hexID = "FZKDFNTQFN281EP5X5P5EP27X27THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TQFN-28-1EP_5x5mm_P0.5mm_EP2.7x2.7mm_ThermalVias', 'description': 'TQFN, 28 Pin (https://pdfserv.maximintegrated.com/package_dwgs/21-0140.PDF (T2855-4)), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'TQFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/TQFN-28-1EP_5x5mm_P0.5mm_EP2.7x2.7mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : TQFN-28-1EP_5x5mm_P0.5mm_EP2.7x2.7mm_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

