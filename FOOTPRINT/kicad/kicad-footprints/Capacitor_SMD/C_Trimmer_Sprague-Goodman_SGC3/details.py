
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Capacitor_SMD"
    oIndex = "C_Trimmer_Sprague-Goodman_SGC3"
    hexID = "FZKCAPACITORSMCTRIERSPRAGUEGOODMANSGC3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'C_Trimmer_Sprague-Goodman_SGC3', 'description': 'trimmer capacitor SMD horizontal, http://media.wix.com/ugd/d86717_38d9821e12823a7aa9cef38c6c2a73cc.pdf', 'tags': ' Sprague Goodman SGC3', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Capacitor_SMD.3dshapes/C_Trimmer_Sprague-Goodman_SGC3.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Capacitor_SMD : C_Trimmer_Sprague-Goodman_SGC3')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

