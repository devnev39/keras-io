ORACLE_MASTER = {
    'path': 'oracles/',
    'title': 'Oracles',
    'toc': True,
    'children': [
        {
            'path': 'base_oracle',
            'title': 'The base Oracle class',
            'generate': [
                'kerastuner.Oracle',
                'kerastuner.Oracle.create_trial',
                'kerastuner.Oracle.end_trial',
                'kerastuner.Oracle.get_best_trials',
                'kerastuner.Oracle.get_state',
                'kerastuner.Oracle.set_state',
                'kerastuner.Oracle.update_trial',
            ]
        },
        {
            'path': 'random',
            'title': 'RandomSearchOracle',
            'generate': [
                'kerastuner.oracles.RandomSearch',
            ]
        },
        {
            'path': 'bayesian',
            'title': 'BayesianOptimizationOracle',
            'generate': [
                'kerastuner.oracles.BayesianOptimization',
            ]
        },
        {
            'path': 'hyperband',
            'title': 'HyperbandOracle',
            'generate': [
                'kerastuner.oracles.Hyperband',
            ]
        },
    ]
}

HYPERMODEL_MASTER = {
    'path': 'hypermodels/',
    'title': 'HyperModels',
    'toc': True,
    'children': [
        {
            'path': 'base_hypermodel',
            'title': 'The base HyperModel class',
            'generate': [
                'kerastuner.HyperModel',
                'kerastuner.HyperModel.build',
            ]
        },
        {
            'path': 'hyper_resnet',
            'title': 'HyperResNet',
            'generate': [
                'kerastuner.applications.HyperResNet',
            ]
        },
        {
            'path': 'hyper_xception',
            'title': 'HyperXception',
            'generate': [
                'kerastuner.applications.HyperXception',
            ]
        },
    ]
}

TUNER_MASTER = {
    'path': 'tuners/',
    'title': 'Tuners',
    'toc': True,
    'children': [
        {
            'path': 'base_tuner',
            'title': 'The base Tuner class',
            'generate': [
                'kerastuner.Tuner',
                'kerastuner.Tuner.get_best_hyperparameters',
                'kerastuner.Tuner.get_best_models',
                'kerastuner.Tuner.get_state',
                'kerastuner.Tuner.load_model',
                'kerastuner.Tuner.on_epoch_begin',
                'kerastuner.Tuner.on_batch_begin',
                'kerastuner.Tuner.on_batch_end',
                'kerastuner.Tuner.on_epoch_end',
                'kerastuner.Tuner.run_trial',
                'kerastuner.Tuner.save_model',
                'kerastuner.Tuner.search',
                'kerastuner.Tuner.set_state',
            ]
        },
        {
            'path': 'random',
            'title': 'RandomSearch',
            'generate': [
                'kerastuner.RandomSearch',
            ]
        },
        {
            'path': 'bayesian',
            'title': 'BayesianOptimization',
            'generate': [
                'kerastuner.BayesianOptimization',
            ]
        },
        {
            'path': 'hyperband',
            'title': 'Hyperband',
            'generate': [
                'kerastuner.Hyperband',
            ]
        },
        {
            'path': 'sklearn',
            'title': 'Sklearn',
            'generate': [
                'kerastuner.tuners.Sklearn',
            ]
        },
    ]
}

KT_API_MASTER = {
    'path': 'keras-tuner/',
    'title': 'Keras Tuner',
    'toc': True,
    'children': [
        {
            'path': 'hyperparameters',
            'title': 'HyperParameters',
            'generate': [
                'kerastuner.HyperParameters',
                'kerastuner.HyperParameters.Boolean',
                'kerastuner.HyperParameters.Choice',
                'kerastuner.HyperParameters.Fixed',
                'kerastuner.HyperParameters.Float',
                'kerastuner.HyperParameters.Int',
                'kerastuner.HyperParameters.conditional_scope',
                'kerastuner.HyperParameters.get',
            ]
        },
        TUNER_MASTER,
        ORACLE_MASTER,
        HYPERMODEL_MASTER,
    ]
}
