#coding:utf-8
'''
循环神经网络
'''
import mxnet as mx
from mxnet import ndarray as nd
from mxnet.gluon import nn
import random
import os
import sys
sys.path.append(os.getcwd())
import utils
from math import exp
from mxnet import autograd
from mxnet import gluon

# 读取数据
with open('datas/jaychou_lyrics.txt',encoding='utf-8') as f:
    corpus_chars = f.read()

corpus_chars = corpus_chars.replace('\n',' ').replace('\t',' ')
corpus_chars = corpus_chars[0:20000]

idx_to_char = list(set(corpus_chars))
char_to_idx = dict([(char,i) for i ,char in enumerate(idx_to_char)])

vocab_size = len(char_to_idx)

print('vocab_size:',vocab_size)

corpus_indices = [char_to_idx[char] for char in corpus_chars]
sample = corpus_indices[:40]
print('chars:\n',''.join([idx_to_char[idx] for idx in sample]))
print('indices:',sample)

# 随机批量采样

def data_iter_random(corpus_indices,batch_size,num_steps,ctx=None):
    num_examples = (len(corpus_chars) - 1) // num_steps
    epoch_size = num_examples // batch_size

    # 随机化样本
    example_indices = list(range(num_examples))
    random.shuffle(example_indices)

    # 返回 num_steps 个数据
    def _data(pos):
        return corpus_indices[pos:pos + num_steps]

    for i in range(epoch_size):
        # 每个读取batch_size 个随机样本
        i = i * batch_size
        batch_indices = example_indices[i : i + batch_size]
        data = nd.array([_data(j * num_steps) for j in batch_indices],ctx=ctx)
        label = nd.array([_data(j * num_steps + 1) for j in batch_indices],ctx=ctx)

        yield data,label

# 相邻批量采样
def data_iter_consecutive(corpus_indices,batch_size,num_steps,ctx=None):
    corpus_indices = nd.array(corpus_indices,ctx=ctx)
    data_len = len(corpus_indices)
    batch_len = data_len // batch_size

    indices = corpus_indices[0:batch_size * batch_len].reshape((
        batch_size,batch_len
    ))

    epoch_size = (batch_len - 1) // num_steps

    for i in range(epoch_size):
        i = i * num_steps
        data = indices[:,i:,i + num_steps]
        label = indices[:,i + 1:i + num_steps + 1]
        yield data,label

# One-hot向量
def get_inputs(data):
    return [nd.one_hot(X,vocab_size) for X in data.T]

# 初始化模型参数

ctx = utils.try_gpu()
input_dim = vocab_size
# 隐含状态长度
hidden_dim = 256
output_dim = vocab_size
scale = 0.01

def get_params():
    # 隐含层
    W_xh = nd.random_normal(scale=scale,shape=(input_dim,hidden_dim),ctx=ctx)
    W_hh = nd.random_normal(scale=scale,shape=(hidden_dim,hidden_dim),ctx=ctx)

    b_h = nd.zeros(hidden_dim,ctx=ctx)

    # 输出层
    W_hy = nd.random_normal(scale=scale,shape=(hidden_dim,output_dim),ctx=ctx)
    b_y = nd.zeros(output_dim,ctx=ctx)

    params = [W_xh,W_hh,b_h,W_hy,b_y]
    for param in params:
        param.attach_grad()

    return params


# 定义模型
# inputs = batch_size * vocab_size
# H = batch_size * hidden_dim
# outputs = batch_size * vocab_size
def rnn(inputs,state,*params):
    H = state
    W_xh,W_hh,b_h,W_hy,b_y = params
    outputs = []
    for X in inputs:
        H = nd.tanh(nd.dot(X,W_xh) + nd.dot(H,W_hh) + b_h)
        Y = nd.dot(H,W_hy) + b_y
        outputs.append(Y)
    return (outputs,H)

# 序列预测
def predict_rnn(rnn,prefix,num_charts,params,hidden_dim,ctx,
                idx_to_char,char_to_idx,get_inputs,is_lstm=False):

    prefix = prefix.lower()
    state_h = nd.zeros(shape=(1,hidden_dim),ctx=ctx)
    if is_lstm:
        # 使用LSTM
        state_c = nd.zeros(shape=(1,hidden_dim),ctx = ctx)
    output = [char_to_idx[prefix[0]]]
    for i in range(num_charts + len(prefix)):
        X = nd.array([output[-1]],ctx=ctx)

        if is_lstm:
            Y,state_h,state_c = rnn(get_inputs(X),state_h,state_c,*params)
        else:
            Y,state_h = rnn(get_inputs(X),state_h,*params)

        if i < len(prefix) - 1:
            next_input = char_to_idx[prefix[i + 1]]
        else:
            next_input = int(Y[0]).argmax(axis=1).asscalar()
        output.append(next_input)
        return ''.join([idx_to_char[i] for i in output])


# 梯度剪裁
def grad_clipping(params,theta,ctx):
    if theta is not None:
        norm = nd.array([0.0],ctx)
        for p in params:
            # print('grad_clipping:grad=',p.grad)
            norm += nd.sum(p.grad ** 2)
            # print('norm:',norm)
        norm = nd.sqrt(norm).asscalar()
        # print('grad_clipoing:norm=%f,theta=%f' %(norm,theta))
        if norm > theta:
            for p in params:
                p.grad[:] *= theta / norm


# 训练
def train_and_predict_rnn(rnn, is_random_iter, epochs, num_steps, hidden_dim, 
                          learning_rate, clipping_norm, batch_size,
                          pred_period, pred_len, seqs, get_params, get_inputs,
                          ctx, corpus_indices, idx_to_char, char_to_idx,
                          is_lstm=False):
    """Train an RNN model and predict the next item in the sequence."""
    if is_random_iter:
        data_iter = data_iter_random
    else:
        data_iter = data_iter_consecutive
    params = get_params()
    
    softmax_cross_entropy = gluon.loss.SoftmaxCrossEntropyLoss()

    for e in range(1, epochs + 1): 
        # If consecutive sampling is used, in the same epoch, the hidden state
        # is initialized only at the beginning of the epoch.
        if not is_random_iter:
            state_h = nd.zeros(shape=(batch_size, hidden_dim), ctx=ctx)
            if is_lstm:
                state_c = nd.zeros(shape=(batch_size, hidden_dim), ctx=ctx)
        train_loss, num_examples = 0, 0
        for data, label in data_iter(corpus_indices, batch_size, num_steps, 
                                     ctx):
            # If random sampling is used, the hidden state has to be
            # initialized for each mini-batch.
            if is_random_iter:
                state_h = nd.zeros(shape=(batch_size, hidden_dim), ctx=ctx)
                if is_lstm:
                    state_c = nd.zeros(shape=(batch_size, hidden_dim), ctx=ctx)
            with autograd.record():
                # outputs shape: (batch_size, vocab_size)
                if is_lstm:
                    outputs, state_h, state_c = rnn(get_inputs(data), state_h,
                                                    state_c, *params) 
                else:
                    outputs, state_h = rnn(get_inputs(data), state_h, *params)
                # Let t_ib_j be the j-th element of the mini-batch at time i.
                # label shape: (batch_size * num_steps)
                # label = [t_0b_0, t_0b_1, ..., t_1b_0, t_1b_1, ..., ].
                label = label.T.reshape((-1,))
                # Concatenate outputs:
                # shape: (batch_size * num_steps, vocab_size).
                outputs = nd.concat(*outputs, dim=0)
                # Now outputs and label are aligned.
                loss = softmax_cross_entropy(outputs, label)
            loss.backward()

            grad_clipping(params, clipping_norm, ctx)
            utils.SGD(params, learning_rate)

            train_loss += nd.sum(loss).asscalar()
            num_examples += loss.size

        if e % pred_period == 0:
            print("Epoch %d. Training perplexity %f" % (e, 
                                               exp(train_loss/num_examples)))
            for seq in seqs:
                print(' - ', predict_rnn(rnn, seq, pred_len, params,
                      hidden_dim, ctx, idx_to_char, char_to_idx, get_inputs,
                      is_lstm))
            print()

epochs = 200
num_steps = 35
learning_rate = 0.1
batch_size = 32

softmax_cross_entropy = gluon.loss.SoftmaxCrossEntropyLoss()

seq1 = '分开'
seq2 = '不分开'
seq3 = '战争中部队'
seqs = [seq1,seq2,seq3]

train_and_predict_rnn(rnn=rnn,is_random_iter=True,
            epochs=200,num_steps=35,
            hidden_dim=hidden_dim,learning_rate=0.2,
            pred_len=5,batch_size=32,pred_period=20,
            clipping_norm=5,seqs=seqs,
            get_params=get_params,
            get_inputs=get_inputs,ctx=ctx,
            corpus_indices=corpus_indices,
            idx_to_char=idx_to_char,
            char_to_idx=char_to_idx)

