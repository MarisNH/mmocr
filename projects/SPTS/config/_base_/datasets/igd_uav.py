igd_uav_textspotting_data_root = 'data/igd_uav'

igd_uav_textspotting_train = dict(
    type='OCRDataset',
    data_root=igd_uav_textspotting_data_root,
    ann_file='textspotting_train.json',
    pipeline=None)

igd_uav_textspotting_test = dict(
    type='OCRDataset',
    data_root=igd_uav_textspotting_data_root,
    ann_file='textspotting_test.json',
    test_mode=True,
    pipeline=None)
