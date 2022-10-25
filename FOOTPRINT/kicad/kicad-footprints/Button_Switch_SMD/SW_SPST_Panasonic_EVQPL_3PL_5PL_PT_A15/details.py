
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Button_Switch_SMD"
    oIndex = "SW_SPST_Panasonic_EVQPL_3PL_5PL_PT_A15"
    hexID = "FZKBSWITCHSMSWSPSTPANASONICEVQPL3PL5PLPTA15"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SW_SPST_Panasonic_EVQPL_3PL_5PL_PT_A15', 'description': 'Light Touch Switch, http://industrial.panasonic.com/cdbs/www-data/pdf/ATK0000/ATK0000CE3.pdf', 'tags': 'SMD SMT SPST EVQPL EVQPT', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Button_Switch_SMD.3dshapes/SW_SPST_Panasonic_EVQPL_3PL_5PL_PT_A15.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Button_Switch_SMD : SW_SPST_Panasonic_EVQPL_3PL_5PL_PT_A15')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

