
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Transistor_Power_Module"
    oIndex = "Infineon_AG-ECONO2"
    hexID = "FZKTRANSISTORPOWERMOINFINEONAGECONO2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Infineon_AG-ECONO2', 'description': '28-lead TH, EconoPACK 2, same as Littelfuse_Package_H_XN2MM, https://www.infineon.com/dgdl/Infineon-FS75R07N2E4-DS-v02_00-en_de.pdf?fileId=db3a30432f5008fe012f52f916333979', 'tags': 'igbt diode module', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Transistor_Power_Module.3dshapes/Infineon_AG-ECONO2.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Transistor_Power_Module : Infineon_AG-ECONO2')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

