igd_uav_textdet_data_root = 'data/igd_uav'

igd_uav_textdet_train = dict(
    type='OCRDataset',
    data_root=igd_uav_textdet_data_root,
    ann_file='textdet_train.json',
    filter_cfg=dict(filter_empty_gt=True, min_size=32),
    pipeline=None)

igd_uav_textdet_test = dict(
    type='OCRDataset',
    data_root=igd_uav_textdet_data_root,
    ann_file='textdet_test.json',
    test_mode=True,
    pipeline=None)
