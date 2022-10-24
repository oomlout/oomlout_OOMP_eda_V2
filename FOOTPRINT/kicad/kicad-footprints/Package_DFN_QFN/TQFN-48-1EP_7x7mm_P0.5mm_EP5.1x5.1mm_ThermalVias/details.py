
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "TQFN-48-1EP_7x7mm_P0.5mm_EP5.1x5.1mm_ThermalVias"
    hexID = "FZKDFNTQFN481EP7X7P5EP51X51THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TQFN-48-1EP_7x7mm_P0.5mm_EP5.1x5.1mm_ThermalVias', 'description': 'TQFN, 48 Pin (https://pdfserv.maximintegrated.com/package_dwgs/21-0144.PDF), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'TQFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/TQFN-48-1EP_7x7mm_P0.5mm_EP5.1x5.1mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : TQFN-48-1EP_7x7mm_P0.5mm_EP5.1x5.1mm_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

