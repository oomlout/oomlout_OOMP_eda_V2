
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Transistor_Power_Module"
    oIndex = "Littelfuse_Package_H_XN2MM"
    hexID = "FZKTRANSISTORPOWERMOLITTELFUPACKAGEHXN2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Littelfuse_Package_H_XN2MM', 'description': '28-lead TH, Package H, same as Infineon_AG-ECONO2, https://www.littelfuse.com/~/media/electronics/datasheets/power_semiconductors/littelfuse_power_semiconductor_igbt_module_mg1225h_xn2mm_datasheet.pdf.pdf', 'tags': 'igbt diode module', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Transistor_Power_Module.3dshapes/Littelfuse_Package_H_XN2MM.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Transistor_Power_Module : Littelfuse_Package_H_XN2MM')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

