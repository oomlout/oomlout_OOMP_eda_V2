
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Transistor_Power_Module"
    oIndex = "ST_ACEPACK-2-CIB"
    hexID = "FZKTRANSISTORPOWERMOSTACEPACK2CIB"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'ST_ACEPACK-2-CIB', 'description': '35-lead TH, ACEPACK 2 CIB, same as Infineon_EasyPIM-2B, https://www.st.com/resource/en/datasheet/a2c25s12m3.pdf', 'tags': 'brifge rectifier igbt diode module', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Transistor_Power_Module.3dshapes/ST_ACEPACK-2-CIB.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Transistor_Power_Module : ST_ACEPACK-2-CIB')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

