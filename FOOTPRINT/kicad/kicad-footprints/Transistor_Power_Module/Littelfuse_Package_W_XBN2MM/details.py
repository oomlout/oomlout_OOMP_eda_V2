
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Transistor_Power_Module"
    oIndex = "Littelfuse_Package_W_XBN2MM"
    hexID = "FZKTRANSISTORPOWERMOLITTELFUPACKAGEWXBN2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Littelfuse_Package_W_XBN2MM', 'description': '24-lead TH, Package W, https://www.littelfuse.com/~/media/electronics/datasheets/power_semiconductors/littelfuse_power_semiconductor_igbt_module_mg1250w_xbn2mm_datasheet.pdf.pdf', 'tags': 'brifge rectifier igbt diode module', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Transistor_Power_Module.3dshapes/Littelfuse_Package_W_XBN2MM.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Transistor_Power_Module : Littelfuse_Package_W_XBN2MM')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

