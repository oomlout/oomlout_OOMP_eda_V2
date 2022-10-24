
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "SO-20-1EP_7.52x12.825mm_P1.27mm_EP6.045x12.09mm_Mask3.56x4.47mm"
    hexID = "FZKSOSO21EP752X12825P127EP645X129MASK356X447"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SO-20-1EP_7.52x12.825mm_P1.27mm_EP6.045x12.09mm_Mask3.56x4.47mm', 'description': 'SO, 20 Pin (http://www.ti.com/lit/ds/symlink/opa569.pdf, http://www.ti.com/lit/an/slma004b/slma004b.pdf), generated with kicad-footprint-generator ipc_gullwing_generator.py', 'tags': 'SO SO', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/SO-20-1EP_7.52x12.825mm_P1.27mm_EP6.045x12.09mm_Mask3.56x4.47mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_SO : SO-20-1EP_7.52x12.825mm_P1.27mm_EP6.045x12.09mm_Mask3.56x4.47mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

