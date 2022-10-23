
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Capacitor_SMD"
    oIndex = "C_Trimmer_Voltronics_JQ"
    hexID = "FZKCAPACITORSMCTRIERVOLTRONICSJQ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'C_Trimmer_Voltronics_JQ', 'description': 'trimmer capacitor SMD horizontal, http://www.knowlescapacitors.com/File%20Library/Voltronics/English/GlobalNavigation/Products/Trimmer%20Capacitors/CerChipTrimCap.pdf', 'tags': ' Voltronics JQ', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Capacitor_SMD.3dshapes/C_Trimmer_Voltronics_JQ.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Capacitor_SMD : C_Trimmer_Voltronics_JQ')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

