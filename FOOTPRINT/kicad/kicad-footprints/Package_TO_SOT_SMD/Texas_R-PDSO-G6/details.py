
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_TO_SOT_SMD"
    oIndex = "Texas_R-PDSO-G6"
    hexID = "FZKPACKAGETOSOTSMTEXASRPDSOG6"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Texas_R-PDSO-G6', 'description': 'R-PDSO-G6, http://www.ti.com/lit/ds/slis144b/slis144b.pdf', 'tags': 'R-PDSO-G6 SC-70-6', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_TO_SOT_SMD.3dshapes/SOT-363_SC-70-6.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_TO_SOT_SMD : Texas_R-PDSO-G6')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

