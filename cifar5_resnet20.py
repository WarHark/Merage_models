config = {
    'dataset': {
        'name': 'cifar50',
    },
    'model': {
        'name': 'resnet20x16',
        'dir': './checkpoints/cifar50_clipv2/resnet20x16/pairsplits',
        'bases': []
    },
    'merging_fn': 'match_tensors_zipit',
    'eval_type': 'clip',
    'merging_metrics': ['covariance', 'mean'],
}