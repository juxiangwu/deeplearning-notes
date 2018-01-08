% 计算线性层的最大学习速率

P = [1 2 -4 7;0.1 3 10 6];
disp('不带阈值学习速度:')
lr1 = maxlinlr(P)
disp('带阈值学习速度:')
lr2 = maxlinlr(P,'bias')