
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "QFN-36-1EP_5x6mm_P0.5mm_EP3.6x4.6mm"
    hexID = "FZKDFNQFN361EP5X6P5EP36X46"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'QFN-36-1EP_5x6mm_P0.5mm_EP3.6x4.6mm', 'description': 'QFN, 36 Pin (https://www.analog.com/media/en/package-pcb-resources/package/pkg_pdf/ltc-legacy-qfn/(UHE36)%20QFN%2005-08-1876%20Rev%20%C3%98.pdf), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'QFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/QFN-36-1EP_5x6mm_P0.5mm_EP3.6x4.6mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : QFN-36-1EP_5x6mm_P0.5mm_EP3.6x4.6mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

