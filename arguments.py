import argparse
def hmnet_arguments():
    parser = argparse.ArgumentParser(description='Point Cloud Registration')
    parser.add_argument('--exp_name', type=str, default='exp', metavar='N',
                        help='Name of the experiment')
    parser.add_argument('--model', type=str, default='hmnet', metavar='N',
                        choices=['hmnet'], help='Model to use, [hmnet]')
    parser.add_argument('--n_emb_dims', type=int, default=512, metavar='N',
                        help='Dimension of embeddings')
    parser.add_argument('--n_iters', type=int, default=3, metavar='N',
                        help='Num of iters to run inference')
    parser.add_argument('--n_keypoints', type=int, default=512, metavar='N',
                        help='Num of keypoints to use')
    parser.add_argument('--train_batch_size', type=int, default=1, metavar='batch_size',
                        help='Size of batch)')
    parser.add_argument('--test_batch_size', type=int, default=1, metavar='batch_size',
                        help='Size of batch)')
    parser.add_argument('--epochs', type=int, default=100, metavar='N',
                        help='number of episode to train ')
    parser.add_argument('--use_sgd', type=bool, default=False,
                        help='Use SGD')
    parser.add_argument('--lr', type=float, default=0.0001, metavar='LR',
                        help='learning rate (default: 0.001, 0.1 if using sgd)')
    parser.add_argument('--momentum', type=float, default=0.9, metavar='M',
                        help='SGD momentum (default: 0.9)')
    parser.add_argument('--no_cuda', action='store_true', default=False,
                        help='enables CUDA training')
    parser.add_argument('--seed', type=int, default=1234, metavar='S',
                        help='random seed (default: 1)')
    parser.add_argument('--eval', action='store_true', default=False,
                        help='evaluate the model')
    parser.add_argument('--discount_factor', type=float, default=0.9, metavar='N',
                        help='')
    parser.add_argument('--gaussian_noise', type=bool, default=True, metavar='N',
                        help='Wheter to add gaussian noise')
    parser.add_argument('--n_points', type=int, default=1024, metavar='N',
                        help='Num of points to use')
    parser.add_argument('--n_subsampled_points', type=int, default=768, metavar='N',
                        help='Num of subsampled points to use')
    parser.add_argument('--dataset', type=str, default='ours', choices=['ours, rpmnet'], metavar='N',
                        help='dataset to use')
    parser.add_argument('--rot_factor', type=float, default=4, metavar='N',
                        help='Divided factor of rotation')
    # the path of model_sampling_k: models/model_sampling_k.t7
    parser.add_argument('--model_path', type=str, default='', metavar='N',
                        help='Pretrained model path')
    parser.add_argument('--temperature', type=float, default=1.0, metavar='N',
                        help='anneal temperature')
    parser.add_argument('--overlap', type=str, default='moderate', metavar='N',
                        help='partial overlapping area, [low, moderate, large]')
    parser.add_argument('--num_workers', default=4, type=int,
                        help='Number of workers for data_loader loader (default: 4).')
    return parser