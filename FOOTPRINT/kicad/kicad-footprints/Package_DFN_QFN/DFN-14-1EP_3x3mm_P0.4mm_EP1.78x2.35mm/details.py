
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "DFN-14-1EP_3x3mm_P0.4mm_EP1.78x2.35mm"
    hexID = "FZKDFNDFN141EP3X3P4EP178X235"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'DFN-14-1EP_3x3mm_P0.4mm_EP1.78x2.35mm', 'description': 'DD Package; 14-Lead Plastic DFN (3mm x 3mm) (http://pdfserv.maximintegrated.com/land_patterns/90-0063.PDF)', 'tags': 'DFN 0.40', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/DFN-14-1EP_3x3mm_P0.4mm_EP1.78x2.35mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DFN_QFN : DFN-14-1EP_3x3mm_P0.4mm_EP1.78x2.35mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

