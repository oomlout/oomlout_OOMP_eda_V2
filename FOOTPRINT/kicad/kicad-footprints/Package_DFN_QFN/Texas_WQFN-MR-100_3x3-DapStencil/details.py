
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "Texas_WQFN-MR-100_3x3-DapStencil"
    hexID = "FZKDFNTEXASWQFNMR13X3DAPSTENCIL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Texas_WQFN-MR-100_3x3-DapStencil', 'description': 'http://www.ti.com/general/docs/lit/getliterature.tsp?baseLiteratureNumber=szza059&fileType=pdf,http://www.ti.com/general/docs/lit/getliterature.tsp?baseLiteratureNumber=mpqf258&fileType=pdf,http://www.ti.com/general/docs/lit/getliterature.tsp?baseLiteratureNumber=LPPD235&fileType=pdf', 'tags': 'MultiRow QFN', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/Texas_WQFN-MR-100.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DFN_QFN : Texas_WQFN-MR-100_3x3-DapStencil')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

