
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Capacitor_SMD"
    oIndex = "C_Trimmer_Murata_TZR1"
    hexID = "FZKCAPACITORSMCTRIERMTZR1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'C_Trimmer_Murata_TZR1', 'description': 'trimmer capacitor SMD horizontal, http://www.murata.com/~/media/webrenewal/support/library/catalog/products/capacitor/trimmer/t13e.ashx?la=en-gb', 'tags': ' Murata TZR1', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Capacitor_SMD.3dshapes/C_Trimmer_Murata_TZR1.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Capacitor_SMD : C_Trimmer_Murata_TZR1')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

