_base_ = [
    '_base_textsnake_resnet50_fpn-unet.py',
    '../_base_/datasets/contNum.py',
    '../_base_/default_runtime.py',
    '../_base_/schedules/schedule_sgd_1200e.py',
]

load_from = 'pths/textsnake_resnet50_fpn-unet_1200e_ctw1500_20220825_221459-c0b6adc4.pth'
train_cfg = dict(type='EpochBasedTrainLoop', max_epochs=100, val_interval=10)
default_hooks = dict(checkpoint=dict(
                        type='CheckpointHook',
                        interval=20,
                        save_last=True,
                        save_best=['icdar/recall', 'icdar/precision', 'icdar/hmean'],
                        rule='greater',
                        _delete_=True),)
# default_hooks = dict(checkpoint=dict(type='CheckpointHook', interval=20, by_epoch=True))

# dataset settings
contNum_textdet_train = _base_.contNum_textdet_train
contNum_textdet_train.pipeline = _base_.train_pipeline
contNum_textdet_test = _base_.contNum_textdet_test
contNum_textdet_test.pipeline = _base_.test_pipeline

train_dataloader = dict(
    batch_size=12,
    num_workers=6,
    persistent_workers=True,
    sampler=dict(type='DefaultSampler', shuffle=True),
    dataset=contNum_textdet_train)

val_dataloader = dict(
    batch_size=1,
    num_workers=1,
    persistent_workers=True,
    sampler=dict(type='DefaultSampler', shuffle=False),
    dataset=contNum_textdet_test)

test_dataloader = val_dataloader

auto_scale_lr = dict(base_batch_size=12)
