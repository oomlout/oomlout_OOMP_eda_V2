
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Transistor_Power_Module"
    oIndex = "Infineon_EasyPIM-2B"
    hexID = "FZKTRANSISTORPOWERMOINFINEONEASYPIM2B"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Infineon_EasyPIM-2B', 'description': '35-lead TH, EasyPIM 2B, same as ST_ACEPACK-2-CIB, https://www.infineon.com/dgdl/Infineon-FP50R06W2E3-DS-v02_02-EN.pdf?fileId=db3a30431b3e89eb011b455c99987d24', 'tags': 'brifge rectifier igbt diode module', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Transistor_Power_Module.3dshapes/Infineon_EasyPIM-2B.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Transistor_Power_Module : Infineon_EasyPIM-2B')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

