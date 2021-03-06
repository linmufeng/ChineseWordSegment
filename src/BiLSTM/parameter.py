'''
    ####file that contains LSTM parameters of this model
    ####modify this file to change LSTM parameters
'''


LEARNING_RATE=0.001                 #学习率
MAX_SENTENCE_SIZE=32                #固定句子长度为32
TIMESTEP_SIZE=MAX_SENTENCE_SIZE     #LSTM的time_step应该和句子长度一致
INPUT_SIZE=EMBEDDING_SIZE=64        #嵌入向量维度,和输入大小应当一样
DECAY=0.85
MAX_EPOCH=3                         #最大迭代次数
LAYER_NUM=2                         #lstm层数2
HIDDEN_UNITS_NUM=128                #隐藏层结点数量
HIDDEN_UNITS_NUM2=128               #隐藏层2结点数量
CLASS_NUM=5                         #类别数量
VOCAB_SIZE=5159                     # 样本中不同字的个数+1(padding 0)，根据处理数据的时候得到
BATCH_SIZE=100                     #batch大小
DROPOUT_RATE=0.5                    #dropout 比率


MODEL_SAVING_PATH="./saved_models/lstm.ckpt"
GRAPH_DEF_SAVING_DIR="./saved_models/"
GRAPH_DEF_SAVING_NAME="lstm.pbtxt"



