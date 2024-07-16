contNum_textspotting_data_root = 'data/containerNum'

contNum_textspotting_train = dict(
    type='OCRDataset',
    data_root=contNum_textspotting_data_root,
    ann_file='textspotting_train.json',
    pipeline=None)

contNum_textspotting_test = dict(
    type='OCRDataset',
    data_root=contNum_textspotting_data_root,
    ann_file='textspotting_test.json',
    test_mode=True,
    pipeline=None)
