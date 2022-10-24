
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "OnSemi_VCT-28_3.5x3.5mm_P0.4mm"
    hexID = "FZKDFNONSEMIVCT2835X35P4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'OnSemi_VCT-28_3.5x3.5mm_P0.4mm', 'description': 'OnSemi  VCT, 28 Pin (http://www.onsemi.com/pub/Collateral/601AE.PDF), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'OnSemi VCT NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/OnSemi_VCT-28_3.5x3.5mm_P0.4mm.wrl', 'pins': {'type': 'smd', 'shape': 'custom'}})
    newPart['name'].append('Package_DFN_QFN : OnSemi_VCT-28_3.5x3.5mm_P0.4mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

