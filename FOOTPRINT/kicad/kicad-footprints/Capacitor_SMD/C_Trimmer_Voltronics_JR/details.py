
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Capacitor_SMD"
    oIndex = "C_Trimmer_Voltronics_JR"
    hexID = "FZKCAPACITORSMCTRIERVOLTRONICSJR"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'C_Trimmer_Voltronics_JR', 'description': 'trimmer capacitor SMD horizontal, http://www.knowlescapacitors.com/File%20Library/Voltronics/English/GlobalNavigation/Products/Trimmer%20Capacitors/CerChipTrimCap.pdf', 'tags': ' Voltronics JR', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Capacitor_SMD.3dshapes/C_Trimmer_Voltronics_JR.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Capacitor_SMD : C_Trimmer_Voltronics_JR')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

