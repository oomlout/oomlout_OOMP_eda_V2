
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Diode_SMD"
    oIndex = "Diode_Bridge_Diotec_SO-DIL-Slim"
    hexID = "FZKDIODESMDIODEBRIDGEDIOTECSODILSLIM"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Diode_Bridge_Diotec_SO-DIL-Slim', 'description': 'SMD diode bridge Diotec SO-DIL Slim, see https://diotec.com/tl_files/diotec/files/pdf/datasheets/b40fs.pdf', 'tags': 'DFS SO-DIL Slim', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Diode_SMD.3dshapes/Diode_Bridge_Diotec_SO-DIL-Slim.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Diode_SMD : Diode_Bridge_Diotec_SO-DIL-Slim')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

