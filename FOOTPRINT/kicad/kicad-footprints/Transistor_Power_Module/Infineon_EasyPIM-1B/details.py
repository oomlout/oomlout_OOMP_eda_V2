
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Transistor_Power_Module"
    oIndex = "Infineon_EasyPIM-1B"
    hexID = "FZKTRANSISTORPOWERMOINFINEONEASYPIM1B"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Infineon_EasyPIM-1B', 'description': '35-lead TH, EasyPIM 1B, https://www.infineon.com/dgdl/Infineon-FP10R06W1E3-DS-v02_01-en_de.pdf?fileId=db3a304412b407950112b43312285a63', 'tags': 'brifge rectifier igbt diode module', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Transistor_Power_Module.3dshapes/Infineon_EasyPIM-1B.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Transistor_Power_Module : Infineon_EasyPIM-1B')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

