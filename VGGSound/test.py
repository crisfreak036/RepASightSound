


class args_dict():
    def __init__(self):
        self.pool = "avgpool"
        self.n_classes = 309
        self.model_depth = 18
        self.resnet_shortcut = 'B'

# def get_arguments():
#     parser = argparse.ArgumentParser()
#     parser.add_argument(
#         '--data_path',
#         default='/scratch/shared/beegfs/hchen/train_data/VGGSound_final/audio/',
#         type=str,
#         help='Directory path of data')
#     parser.add_argument(
#         '--result_path',
#         default='/scratch/shared/beegfs/hchen/prediction/audioclassification/vggsound/resnet18/',
#         type=str,
#         help='Directory path of results')
#     parser.add_argument(
#         '--summaries',
#         default='/scratch/shared/beegfs/hchen/epoch/audioclassification_f/resnet18_vlad/model.pth.tar',
#         type=str,
#         help='Directory path of pretrained model')
#     parser.add_argument(
#         '--pool',
#         default="avgpool",
#         type=str,
#         help= 'either vlad or avgpool')
#     parser.add_argument(
#         '--csv_path',
#         default='./data/',
#         type=str,
#         help='metadata directory')
#     parser.add_argument(
#         '--test',
#         default='test.csv',
#         type=str,
#         help='test csv files')
#     parser.add_argument(
#         '--batch_size',
#         default=32,
#         type=int,
#         help='Batch Size')
#     parser.add_argument(
#         '--n_classes',
#         default=309,
#         type=int,
#         help=
#         'Number of classes')
#     parser.add_argument(
#         '--model_depth',
#         default=18,
#         type=int,
#         help='Depth of resnet (10 | 18 | 34 | 50 | 101)')
#     parser.add_argument(
#         '--resnet_shortcut',
#         default='B',
#         type=str,
#         help='Shortcut type of resnet (A | B)')
#     return parser.parse_args()



# def main():
#     args = get_arguments()
#
#     # create prediction directory if not exists
#     if not os.path.exists(args.result_path):
#         os.mkdir(args.result_path)
#
#     # init network
#     os.environ["CUDA_VISIBLE_DEVICES"]="0"
#     model= AVENet(args)
#     device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
#     model = model.cuda()
#
#     # load pretrained models
#     checkpoint = torch.load(args.summaries)
#     model.load_state_dict(checkpoint['model_state_dict'])
#     model.to(device)
#     print('load pretrained model.')
#
#     # create dataloader
#     testdataset = GetAudioVideoDataset(args,  mode='test')
#     testdataloader = DataLoader(testdataset, batch_size=args.batch_size, shuffle=False,num_workers = 16)
#
#     softmax = nn.Softmax(dim=1)
#     print("Loaded dataloader.")
#
#     model.eval()
#     for step, (spec, audio, label, name) in enumerate(testdataloader):
#         print('%d / %d' % (step,len(testdataloader) - 1))
#         spec = Variable(spec).cuda()
#         label = Variable(label).cuda()
#         aud_o = model(spec.unsqueeze(1).float())
#
#         prediction = softmax(aud_o)
#
#         for i, item in enumerate(name):
#             np.save(args.result_path + '/%s.npy' % item,prediction[i].cpu().data.numpy())
#
#
#
# if __name__ == "__main__":
#     main()

