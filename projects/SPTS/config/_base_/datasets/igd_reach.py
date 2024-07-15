igd_reach_textspotting_data_root = 'data/igd_reach'

igd_reach_textspotting_train = dict(
    type='OCRDataset',
    data_root=igd_reach_textspotting_data_root,
    ann_file='textspotting_train.json',
    pipeline=None)

igd_reach_textspotting_test = dict(
    type='OCRDataset',
    data_root=igd_reach_textspotting_data_root,
    ann_file='textspotting_test.json',
    test_mode=True,
    pipeline=None)
