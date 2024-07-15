contNum_textrecog_data_root = "data/ContainerNum"

contNum_textrecog_train = dict(
    type="OCRDataset",
    data_root=contNum_textrecog_data_root,
    ann_file="textrecog_train.json",
    pipeline=None,
)

contNum_textrecog_test = dict(
    type="OCRDataset",
    data_root=contNum_textrecog_data_root,
    ann_file="textrecog_test.json",
    test_mode=True,
    pipeline=None,
)
