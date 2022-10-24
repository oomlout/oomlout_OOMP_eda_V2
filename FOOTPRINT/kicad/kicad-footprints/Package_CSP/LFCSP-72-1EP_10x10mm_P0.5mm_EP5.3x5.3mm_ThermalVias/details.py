
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_CSP"
    oIndex = "LFCSP-72-1EP_10x10mm_P0.5mm_EP5.3x5.3mm_ThermalVias"
    hexID = "FZKCSPLFCSP721EP1X1P5EP53X53THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LFCSP-72-1EP_10x10mm_P0.5mm_EP5.3x5.3mm_ThermalVias', 'description': 'LFCSP, 72 Pin (http://www.analog.com/media/en/technical-documentation/data-sheets/ADAU1452_1451_1450.pdf), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'LFCSP NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_CSP.3dshapes/LFCSP-72-1EP_10x10mm_P0.5mm_EP5.3x5.3mm.wrl', 'pins': {'type': 'smd', 'shape': 'custom'}})
    newPart['name'].append('Package_CSP : LFCSP-72-1EP_10x10mm_P0.5mm_EP5.3x5.3mm_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

