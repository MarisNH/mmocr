igd_ground_textrecog_data_root = "data/igd_ground"

igd_ground_textrecog_train = dict(
    type="OCRDataset",
    data_root=igd_ground_textrecog_data_root,
    ann_file="textrecog_train.json",
    pipeline=None,
)

igd_ground_textrecog_test = dict(
    type="OCRDataset",
    data_root=igd_ground_textrecog_data_root,
    ann_file="textrecog_test.json",
    test_mode=True,
    pipeline=None,
)
