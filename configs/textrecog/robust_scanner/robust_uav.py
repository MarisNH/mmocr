_base_ = [
    "../_base_/datasets/igd_uav.py",
    "../_base_/default_runtime.py",
    "../_base_/schedules/schedule_adam_step_5e.py",
    "_base_robustscanner_resnet31.py",
]

load_from = 'pths/robustscanner_resnet31_5e_st-sub_mj-sub_sa_real_20220915_152447-7fc35929.pth'
train_cfg = dict(type='EpochBasedTrainLoop', max_epochs=100, val_interval=10)

# dataset settings
train_list = [_base_.igd_uav_textrecog_train]
test_list = [_base_.igd_uav_textrecog_test]

default_hooks = dict(checkpoint=dict(
                        type='CheckpointHook',
                        interval=50,
                        save_best=['IC15/recog/char_recall', 'IC15/recog/char_precision'],
                        rule='greater',
                        _delete_=True),)

train_dataloader = dict(
    batch_size=16,
    num_workers=4,
    persistent_workers=True,
    sampler=dict(type="DefaultSampler", shuffle=True),
    dataset=dict(
        type="ConcatDataset", datasets=train_list, pipeline=_base_.train_pipeline
    ),
)

val_dataloader = dict(
    batch_size=1,
    num_workers=4,
    persistent_workers=True,
    drop_last=False,
    sampler=dict(type="DefaultSampler", shuffle=False),
    dataset=dict(
        type="ConcatDataset", datasets=test_list, pipeline=_base_.test_pipeline
    ),
)
test_dataloader = val_dataloader

val_evaluator = dict(dataset_prefixes=["IC15"])
test_evaluator = val_evaluator

auto_scale_lr = dict(base_batch_size=16)