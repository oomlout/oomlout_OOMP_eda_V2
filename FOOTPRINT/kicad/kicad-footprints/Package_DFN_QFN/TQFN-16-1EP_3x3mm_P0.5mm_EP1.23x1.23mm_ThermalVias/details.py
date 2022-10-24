
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "TQFN-16-1EP_3x3mm_P0.5mm_EP1.23x1.23mm_ThermalVias"
    hexID = "FZKDFNTQFN161EP3X3P5EP123X123THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TQFN-16-1EP_3x3mm_P0.5mm_EP1.23x1.23mm_ThermalVias', 'description': 'TQFN, 16 Pin (https://pdfserv.maximintegrated.com/package_dwgs/21-0136.PDF (T1633-5), https://pdfserv.maximintegrated.com/land_patterns/90-0032.PDF), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'TQFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/TQFN-16-1EP_3x3mm_P0.5mm_EP1.23x1.23mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : TQFN-16-1EP_3x3mm_P0.5mm_EP1.23x1.23mm_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

