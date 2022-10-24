
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "WDFN-12-1EP_3x3mm_P0.45mm_EP1.7x2.5mm"
    hexID = "FZKDFNWDFN121EP3X3P45EP17X25"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'WDFN-12-1EP_3x3mm_P0.45mm_EP1.7x2.5mm', 'description': 'WDFN, 12 Pin (https://www.diodes.com/assets/Datasheets/PAM2306.pdf), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'WDFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/WDFN-12-1EP_3x3mm_P0.45mm_EP1.7x2.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : WDFN-12-1EP_3x3mm_P0.45mm_EP1.7x2.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

