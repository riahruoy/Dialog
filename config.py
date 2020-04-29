class Config:
    seed = 116
    device = 'cpu'

    n_epoch = 100
    batch_size = 1
    max_len = 22

    vocab_size = 32000
    num_head = 8
    d_model = 768
    num_layer = 6
    d_ff = 2048
    drop_rate = 0.1
    max_grad_norm = 1.0
    max_data_size = 10000

    smoothing = 0.1
    factor = 2
    warmup = 4000

    # FIXME: Data path must be changed.
    data_dir = './data'
    train_data_path = f'{data_dir}/fce.dev.gold.bea19.m2.tsv'
    pickle_path = f'{data_dir}/train_data.pkl'
    fn = 'ckpt'

    load = False
    # FIXME: if you use original data, change flag of this
    use_pickle = False

    model_name = 'bert-base-uncased'
