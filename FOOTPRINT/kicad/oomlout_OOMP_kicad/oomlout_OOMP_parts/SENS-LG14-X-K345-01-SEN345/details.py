
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "SENS-LG14-X-K345-01-SEN345"
    hexID = "FZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSSENSLG14XK3451SEN345"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SENS-LG14-X-K345-01-SEN345', 'description': 'hexID: SEN345; LGA, 14 Pin (http://www.st.com/resource/en/datasheet/lsm303dlhc.pdf), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'LGA NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_LGA.3dshapes/LGA-14_3x5mm_P0.8mm_LayoutBorder1x6y.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('oomlout_OOMP_parts : SENS-LG14-X-K345-01-SEN345')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

