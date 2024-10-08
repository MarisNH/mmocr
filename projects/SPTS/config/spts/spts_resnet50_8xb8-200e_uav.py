_base_ = [
    '_base_spts_resnet50_mmocr.py',
    '../_base_/datasets/igd_uav.py',
    '../_base_/default_runtime.py',
]

load_from = 'pths/spts_resnet50_150e_pretrain-spts-c9fe4c78.pth'

num_epochs = 20
lr = 0.00001

default_hooks = dict(
    checkpoint=dict(
        type='CheckpointHook',
        interval=10,
        save_best='none/hmean',
        rule='greater',
        _delete_=True))

optim_wrapper = dict(
    type='OptimWrapper',
    optimizer=dict(type='AdamW', lr=lr, weight_decay=0.0001),
    paramwise_cfg=dict(custom_keys={
        'backbone': dict(lr_mult=0.1),
    }))

train_cfg = dict(
    type='EpochBasedTrainLoop', max_epochs=num_epochs, val_interval=5)
val_cfg = dict(type='ValLoop')
test_cfg = dict(type='TestLoop')

# dataset settings
igd_uav_textspotting_train = _base_.igd_uav_textspotting_train
igd_uav_textspotting_train.pipeline = _base_.train_pipeline
igd_uav_textspotting_test = _base_.igd_uav_textspotting_test
igd_uav_textspotting_test.pipeline = _base_.test_pipeline

train_dataloader = dict(
    batch_size=3,
    num_workers=4,
    persistent_workers=True,
    pin_memory=True,
    sampler=dict(type='BatchAugSampler', shuffle=True, num_repeats=1), #was 2
    dataset=igd_uav_textspotting_train)

val_dataloader = dict(
    batch_size=1,
    num_workers=4,
    persistent_workers=True,
    pin_memory=True,
    sampler=dict(type='DefaultSampler', shuffle=False),
    dataset=igd_uav_textspotting_test)

test_dataloader = val_dataloader

val_cfg = dict(type='ValLoop')
test_cfg = dict(type='TestLoop')

val_evaluator = [
    dict(
        type='E2EPointMetric',
        prefix='none',
        word_spotting=True,
        match_dist_thr=0.4),
]

test_evaluator = val_evaluator
