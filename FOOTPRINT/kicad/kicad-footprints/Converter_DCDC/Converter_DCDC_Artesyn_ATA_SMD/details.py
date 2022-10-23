
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Converter_DCDC"
    oIndex = "Converter_DCDC_Artesyn_ATA_SMD"
    hexID = "FZKCONCONARTESYNATASM"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Converter_DCDC_Artesyn_ATA_SMD', 'description': 'DCDC-Converter, Artesyn, ATA Series, 3W Single and Dual Output, 1500VDC Isolation, 24.0x13.7x8.0mm https://www.artesyn.com/power/assets/ata_series_ds_01apr2015_79c25814fd.pdf https://www.artesyn.com/power/assets/trn_dc-dc_ata_3w_series_releas1430412818_techref.pdf', 'tags': 'DCDC SMD', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Converter_DCDC.3dshapes/Converter_DCDC_Artesyn_ATA_SMD.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Converter_DCDC : Converter_DCDC_Artesyn_ATA_SMD')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

